# -*- mode: ruby -*-
# vi: set ft=ruby :

$provisioning_script = <<SCRIPT
fail() {
   echo "failed to $1"
   exit 1
}

if [ ! -f /home/vagrant/provision-complete ]; then
    echo "Running provisioning script"
    set -x

    curl -s https://downloads.perfsonar.net/install | sh -s - testpoint

    touch /home/vagrant/provision-complete
fi
sudo apt-get update
sudo apt-get -y upgrade
SCRIPT

Vagrant.configure("2") do |config|
  config.vm.box = "generic/ubuntu2204"

  config.vm.synced_folder ".", "/vagrant", disabled: true

  config.ssh.forward_agent = true
  config.vm.hostname = "esnet-portal.local"

  config.vm.network :private_network, ip: "192.168.56.11"
  config.vm.network :forwarded_port, guest: 22, host: 22011, id: 'ssh'

  config.vm.provision :shell, :inline => $provisioning_script

  config.vm.provider "virtualbox" do |v|
    v.name = "psconfig.local"
    v.memory = 1024
  end
end
