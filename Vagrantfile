Vagrant.configure("2") do |config|

  config.vm.provider "virtualbox" do |v|
    v.memory = 2048
    v.cpus   = 4
      config.vm.provider "virtualbox" do |vb|
    	vb.customize [ "modifyvm", :id, "--uartmode1", "disconnected" ]
  	  end
  end
  
  config.vm.box = "bento/ubuntu-19.10"  
  config.vm.network "private_network", ip: "192.168.56.111"
  config.vm.provision :docker
  config.vm.provision :docker_compose, yml: "/vagrant/docker-compose.yml", rebuild: true, run: "always"
 
end
