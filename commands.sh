# Create s3 bucket for SAM use
aws s3 mb s3://yoni2k-first-sam1

# package cloudformation from SAM template
aws cloudformation package --s3-bucket yoni2k-first-sam1 --template-file template.yaml --output-template-file gen/template-generated.yaml

# deploy cloudformation template
aws cloudformation deploy --template-file gen\template-generated.yaml --stack-name hello-world-sam --capabilities CAPABILITY_IAM
