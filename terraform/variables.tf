variable "aws_region" {
  type    = string
  default = "eu-north-1" 
}

variable "instance_type" {
  type    = string
  default = "t3.micro"
}

variable "ssh_public_key" {
  type        = string
  description = "Your SSH public key for server access"
}