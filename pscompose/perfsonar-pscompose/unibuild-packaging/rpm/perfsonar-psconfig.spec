%define install_base        /usr/lib/perfsonar
%define pscompose_base      %{install_base}/pscompose
%define config_base         /etc/perfsonar/pscompose
%define httpd_config_base   /etc/httpd/conf.d
%define systemd_base        /usr/lib/systemd/system

#Version variables set by automated scripts
%define perfsonar_auto_version 5.3.0
%define perfsonar_auto_relnum 0.a1.0

Name:			perfsonar-pscompose
Version:		%{perfsonar_auto_version}
Release:		%{perfsonar_auto_relnum}%{?dist}
Summary:		perfSONAR pSCompose
License:		ASL 2.0
Group:			Development/Libraries
URL:			http://www.perfsonar.net
Source0:		perfsonar-pscompose-%{version}.tar.gz
BuildArch:		noarch
# The venv contains compiled .so extensions; disable debuginfo/debugsource
# sub-packages to avoid unpackaged debug file errors
%global debug_package %{nil}
BuildRequires:  systemd-rpm-macros
BuildRequires:  python3
BuildRequires:  python3-pip
#Requires:       perfsonar-common
#Requires: pscheduler-bundle-full
Requires:       python3
Requires:       postgresql
Requires:       postgresql-contrib
Requires:       postgresql-devel
Requires:       postgresql-libs
Requires:       postgresql-plpython3
Requires:       postgresql-server
Requires:       httpd
Requires:       mod_ssl
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%description
A package that installs the perfSONAR pSCompose user interface for configuring measurements.

%prep
%setup -q -n %{name}-%{version}

#TODO: Add back perfsonar-common and delete below
%pre
/usr/sbin/groupadd -r perfsonar 2> /dev/null || :
/usr/sbin/useradd -g perfsonar -r -s /sbin/nologin -c "perfSONAR User" -d /tmp perfsonar 2> /dev/null || :

%build

%install
make ROOTPATH=%{buildroot}%{pscompose_base} CONFIGPATH=%{buildroot}%{config_base} HTTPD-CONFIGPATH=%{buildroot}/%{httpd_config_base} SYSTEMD-CONFIGPATH=%{buildroot}/%{systemd_base} VENVPATH=%{buildroot}%{pscompose_base}/venv install
# Rewrite embedded buildroot paths in the venv so it works at install-time location
find %{buildroot}%{pscompose_base}/venv -type f \
    -exec grep -ql '%{buildroot}' {} \; \
    -exec sed -i 's|%{buildroot}||g' {} \;
# Replace the absolute python3 symlink with a relative one to avoid rpmlint error
ln -sf ../../../../../bin/python3 \
    %{buildroot}%{pscompose_base}/venv/bin/python3 2>/dev/null || true
# Remove test directories from venv site-packages to avoid ambiguous shebang errors
find %{buildroot}%{pscompose_base}/venv/lib -type d -name tests \
    -path "*/site-packages/*" -exec rm -rf {} +
# Rewrite ambiguous '#!/usr/bin/env python' shebangs to python3
find %{buildroot}%{pscompose_base}/venv/lib -name "*.py" \
    -exec grep -qm1 '^#!/usr/bin/env python$' {} \; \
    -exec sed -i 's|^#!/usr/bin/env python$|#!/usr/bin/env python3|' {} \;
# Remove pre-compiled bytecode from the venv: it was compiled by the build
# container's Python, which may be a different version than the system Python
# on the target machine.  Python will recompile .pyc files on first import.
find %{buildroot}%{pscompose_base}/venv -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
find %{buildroot}%{pscompose_base}/venv -name "*.pyc" -delete 2>/dev/null || true
# Do the same for the pscompose package itself
find %{buildroot}%{pscompose_base}/pscompose -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
find %{buildroot}%{pscompose_base}/pscompose -name "*.pyc" -delete 2>/dev/null || true
# Strip executable bit from all venv non-script files (metadata, headers, configs, etc.)
find %{buildroot}%{pscompose_base}/venv/lib -type f -executable \
    ! -exec grep -qm1 '^#!' {} \; -exec chmod -x {} \;
find %{buildroot}%{pscompose_base}/venv/pyvenv.cfg -executable 2>/dev/null \
    -exec chmod -x {} \;
find %{buildroot}%{pscompose_base}/venv/include -type f -executable \
    -exec chmod -x {} \;
# Strip executable bit from all frontend static files
find %{buildroot}%{pscompose_base}/frontend -type f -executable \
    ! -exec grep -qm1 '^#!' {} \; -exec chmod -x {} \;
# Strip executable bit from systemd unit files
chmod -x %{buildroot}%{systemd_base}/perfsonar-pscompose.service \
         %{buildroot}%{systemd_base}/perfsonar-pscompose.socket \
         %{buildroot}%{systemd_base}/perfsonar-pscompose-frontend.service

%clean
rm -rf %{buildroot}

%post
%systemd_post perfsonar-pscompose.socket perfsonar-pscompose.service perfsonar-pscompose-frontend.service
if [ "$1" = "1" ]; then
    # Run the PostgreSQL database setup script
    %{pscompose_base}/scripts/pg_setup.sh
    # Fresh install: enable and start the socket, frontend, and Apache
    systemctl enable --now perfsonar-pscompose.socket
    systemctl enable --now perfsonar-pscompose-frontend.service
    systemctl enable httpd
    systemctl restart httpd
fi
if [ "$1" = "2" ]; then
    # Upgrade: reload services
    systemctl try-restart perfsonar-pscompose.service
    systemctl try-restart perfsonar-pscompose-frontend.service
fi

%preun
%systemd_preun perfsonar-pscompose.socket perfsonar-pscompose.service perfsonar-pscompose-frontend.service

%postun
%systemd_postun_with_restart perfsonar-pscompose.service perfsonar-pscompose-frontend.service

%files
%defattr(0644,perfsonar,perfsonar,0755)
%config(noreplace) %{config_base}/settings.yml
%{pscompose_base}/pscompose/
%{pscompose_base}/frontend/
%{pscompose_base}/venv/
%attr(0755, perfsonar, perfsonar) %{pscompose_base}/venv/bin/
%attr(0644, root, root) %{httpd_config_base}/apache-pscompose.conf
%attr(0644, root, root) %{systemd_base}/perfsonar-pscompose.service
%attr(0644, root, root) %{systemd_base}/perfsonar-pscompose.socket
%attr(0644, root, root) %{systemd_base}/perfsonar-pscompose-frontend.service
%attr(0755, root, root) %{pscompose_base}/scripts/pg_setup.sh

%changelog
* Thu Aug 27 2026 Andy Lake <andy@es.net> - 5.3.0-0.a1.0
- Initial package