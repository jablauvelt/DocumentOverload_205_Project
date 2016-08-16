# Setup AWS CLI (Command Line Interface)

1. In Bash on core AWS instance: `pip install awscli`
2. In AWS console:
  1.	Click on name at top right
  2.	Security credentials
  3.	Click on + next to Access Keys (Access Key ID and Secret Access Key)
  4.	Create new Access Key
  5.	Note these values
3. In Bash on AWS instance: `aws configure`
4. Enter Key ID and Access Key for the first two prompts, then "us-east-1" for the third, then just press Enter for the fourth prompt.
5. Test: `aws help`

# Setup S3

1. Create an S3 bucket in AWS S3 called "docoverload" (or something similar, if that name is taken. Anywhere in the rest of this repository that you see a reference to "docoverload", instead insert the name of your bucket). The process should be pretty straightforward - just make sure it's in the US East.

# Upload .txt files to S3

In Bash on AWS instance:

1. Upload the single combined file txt file: `aws s3 cp /enron_output/enron_emails_text_all.txt s3://docoverload`

