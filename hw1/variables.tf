variable "aws_region" {
  description = "AWS region for infrastructure"
  type        = string
}

variable "project_name" {
  description = "Project name"
  type        = string
  default     = "homework-1"
}

variable "s3_bucket_name" {
  description = "Name of the S3 data bucket"
  type        = string
}

variable "ec2_instance_name" {
  description = "Name of the EC2 instance"
  type        = string
}

variable "ec2_instance_type" {
  description = "EC2 instance type"
  type        = string
}

variable "redshift_cluster_name" {
  description = "Name of the Redshift cluster"
  type        = string
}

variable "redshift_node_type" {
  description = "Redshift DB password"
  type        = string
}

variable "db_name" {
  description = "Redshift DB name"
  type        = string
}

variable "db_username" {
  description = "Redshift DB username"
  type        = string
}

variable "db_password" {
  description = "Redshift DB password"
  type        = string
}
