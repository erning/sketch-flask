# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "hashicorp/precise64"
  config.vm.network :private_network, ip: "192.168.222.2"

  config.vm.provision "shell",
    inline: "mkdir -p /root/.ssh/ && grep -m 1 -q vagrant /root/.ssh/authorized_keys || cp /home/vagrant/.ssh/authorized_keys /root/.ssh/"

  config.vm.provision :ansible do |ansible|
    ansible.inventory_path = '.provision/hosts.vagrant'
    ansible.playbook = '.provision/playbook.yml'
    ansible.host_key_checking = false
    ansible.limit = 'vagrant'
    # ansible.verbose = 'vvvv'
  end
end
