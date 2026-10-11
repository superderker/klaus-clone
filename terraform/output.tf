output "instance_public_ip" {
  description = "Public IP address of the Klaus server"
  value       = aws_instance.klaus_host.public_ip
}