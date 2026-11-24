
output "instance_hostname" {
  description = "Private DNS name of the EC2 instance"
  value       = aws_instance.app_server.private_dns
}

output "private_ip" {
  description = "Private IP of the EC2 instance"
  value       = aws_instance.app_server.private_ip
}

output "public_ip" {
  description = "Public IP of the EC2 instance"
  value       = aws_instance.app_server.public_ip
}
