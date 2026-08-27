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
BuildRequires:  systemd-rpm-macros
Requires:       perfsonar-common
Requires:       python3
Requires:       python3-fastapi
Requires:       python3-sqlalchemy
Requires:       python3-pydantic
Requires:       python3-bcrypt
Requires:       python3-uvicorn
Requires:       python3-gunicorn
Requires:       python3-multipart
Requires:       python3-requests
Requires:       python3-psycopg2
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

%build

%install
make ROOTPATH=%{buildroot}%{pscompose_base} CONFIGPATH=%{buildroot}%{config_base} HTTPD-CONFIGPATH=%{buildroot}/%{httpd_config_base} SYSTEMD-CONFIGPATH=%{buildroot}/%{systemd_base} install

%clean
rm -rf %{buildroot}

%post
%systemd_post perfsonar-pscompose.socket perfsonar-pscompose.service
if [ "$1" = "1" ]; then
    # Fresh install: enable and start the socket and Apache
    systemctl enable --now perfsonar-pscompose.socket
    systemctl enable httpd
    systemctl restart httpd
fi
if [ "$1" = "2" ]; then
    # Upgrade: reload service
    systemctl try-restart perfsonar-pscompose.service
fi

%preun
%systemd_preun perfsonar-pscompose.socket perfsonar-pscompose.service

%postun
%systemd_postun_with_restart perfsonar-pscompose.service

%files
%defattr(0644,perfsonar,perfsonar,0755)
%config(noreplace) %{config_base}/settings.yml
%{pscompose_base}/pscompose/
%exclude %{pscompose_base}/pscompose/**/*.pyc
%exclude %{pscompose_base}/pscompose/**/*.pyo
%exclude %{pscompose_base}/pscompose/**/__pycache__
%{pscompose_base}/pscompose/frontend
%attr(0644, root, root) %{httpd_config_base}/apache-pscompose.conf
%attr(0644, root, root) %{systemd_base}/perfsonar-pscompose.service
%attr(0644, root, root) %{systemd_base}/perfsonar-pscompose.socket

%changelog
* Thu Aug 27 2026 Andy Lake <andy@es.net> - 5.3.0-0.a1.0
- Initial package