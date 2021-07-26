# Devops: infra automation with terraforms
# https://www.udemy.com/course/learn-devops-infrastructure-automation-with-terraform
# github: https://github.com/wardviaene/terraform-course
# Slides: http://assets.in4it.s3.amazonaws.com/public/udemy/learn-devops-terraform-dec2020.pdf

# course covers
# install terraforms
# provisioning, modules, state
# terraform to provision infra on aws - virtual private cloud, iam roles, autoscaing
# using packer with terraform
# docker
# jenkins workflow

# objective
# use and apply terraform
# features terraform
# use with aws
# use with packer and custom images

# what it is
# infra as code
# either you can use webconsole of aws or other cloud or you can even automate
# keep infra in certain state (i.e. configuration management)
# infra changes can be kept in version control system like git

# ansible, chef, puppet, saltstack have a focus on automating the installation and configuratio of software
# and to keep machine in compliance, in certain state
# while terraform can automate provisioning of the infra itself ie. on aws, digitalocean, azure api
# terraform works with ansible

# example: spin up a machine using terraform, and use ansible to configure that machine
# so both terraform and ansible work together