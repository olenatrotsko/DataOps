# S3
output "s3_bucket_name" {
  description = "S3 bucket name"
  value       = aws_s3_bucket.storage.bucket
}

output "s3_bucket_arn" {
  description = "S3 bucket ARN"
  value       = aws_s3_bucket.storage.arn
}

# EC2
output "ec2_instance_id" {
  description = "EC2 instance ID"
  value       = aws_instance.vm.id
}

output "ec2_public_ip" {
  description = "EC2 public IP address"
  value       = aws_instance.vm.public_ip
}

output "ec2_private_ip" {
  description = "EC2 private IP address"
  value       = aws_instance.vm.private_ip
}

# Redshift Serverless
output "redshift_endpoint" {
  description = "Redshift Serverless endpoint"
  value       = aws_redshift_cluster.cluster.endpoint
}
