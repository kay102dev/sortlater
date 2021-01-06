{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "iam:CreateRole",
                "s3:CreateBucket",
                "iam:AttachRolePolicy",
                "cloudformation:CreateChangeSet",
                "iam:PutRolePolicy",
                "s3:GetBucketPolicy",
                "cloudformation:DeleteChangeSet",
                "s3:PutEncryptionConfiguration",
                "s3:GetEncryptionConfiguration",
                "cloudformation:DescribeStackEvents",
                "iam:DetachRolePolicy",
                "iam:DeleteRolePolicy",
                "cloudformation:UpdateStack",
                "s3:PutBucketAcl",
                "cloudformation:DescribeChangeSet",
                "cloudformation:ExecuteChangeSet",
                "s3:DeleteBucket",
                "s3:GetBucketPublicAccessBlock",
                "s3:GetBucketPolicyStatus",
                "iam:GetRole",
                "s3:PutBucketPublicAccessBlock",
                "ecr:CreateRepository",
                "iam:DeleteRole",
                "iam:PassRole",
                "cloudformation:DescribeStacks",
                "cloudformation:CreateStack",
                "cloudformation:GetTemplate",
                "cloudformation:DeleteStack",
                "s3:PutBucketPolicy"
            ],
            "Resource": [
                "arn:aws:cloudformation:eu-west-1:398188212409:stack/CDKToolkit/*",
                "arn:aws:iam::029549140631:role/cdk-*-file-publishing-role-029549140631-*",
                "arn:aws:iam::029549140631:role/cdk-*-image-publishing-role-029549140631-*",
                "arn:aws:iam::029549140631:role/cdk-*-deploy-role-029549140631-*",
                "arn:aws:iam::029549140631:role/cdk-*-cfn-exec-role-029549140631-*",
                "arn:aws:iam::029549140631:role/*-PipelineBuildSynthCodePipel*",
                "arn:aws:iam::029549140631:role/*-PipelineUpdatePipelineSelfM*",
                "arn:aws:iam::029549140631:role/*-BuildRole*",
                "arn:aws:iam::029549140631:role/*-PipelineToBuildStageToBuild*",
                "arn:aws:iam::029549140631:role/*-PipelineAssetsFileRole*",
                "arn:aws:iam::029549140631:role/*-PipelineRole*",
                "arn:aws:iam::029549140631:role/*-PipelineBuildSynthCdkBuildP*",
                "arn:aws:s3:::cdk*-assets-029549140631-*",
                "arn:aws:s3:::*",
                "arn:aws:ecr:eu-west-1:029549140631:repository/cdk-*-container-assets-029549140631-*",
                "arn:aws:iam::029549140631:role/*-PipelineBuildSynthCdkBuildP*",
                "arn:aws:iam::029549140631:role/*-PipelineAssetsFileRole59943*",
                "arn:aws:iam::029549140631:role/*-PipelineUpdatePipelineSelfM*",
                "arn:aws:iam::029549140631:role/*-PipelineBuildSynthCdkBuildP*",
                "arn:aws:iam::029549140631:role/*-BuildRole*"
            ]
        },
        {
            "Sid": "VisualEditor1",
            "Effect": "Allow",
            "Action": [
                "ecr:DescribeRepositories",
                "ecr:DeleteRepository"
            ],
            "Resource": "arn:aws:ecr:*:398188212409:repository/*"
        },
        {
            "Sid": "VisualEditor2",
            "Effect": "Allow",
            "Action": [
                "kms:Create*",
                "kms:List*",
                "kms:Update*",
                "kms:Get*",
                "kms:Describe*",
                "kms:CancelKeyDeletion",
                "ssm:GetParameters",
                "ssm:PutParameter",
                "ssm:DeleteParameter",
                "kms:Revoke*",
                "kms:Disable*",
                "ssm:AddTagsToResource",
                "kms:ScheduleKeyDeletion",
                "kms:Delete*",
                "kms:Enable*",
                "kms:Put*"
            ],
            "Resource": "*"
        },
        {
            "Sid": "VisualEditor3",
            "Effect": "Allow",
            "Action": [
                "s3:PutAccountPublicAccessBlock",
                "s3:GetAccountPublicAccessBlock",
                "s3:PutAccessPointPublicAccessBlock"
            ],
            "Resource": "arn:aws:s3:::cdk*-assets-398188212409-*"
        },
        {
            "Sid": "VisualEditor4",
            "Effect": "Allow",
            "Action": [
                "codebuild:CreateProject",
                "codebuild:BatchGetBuilds",
                "codebuild:StartBuild",
                "codebuild:DeleteProject",
                "codebuild:BatchGetProjects"
            ],
            "Resource": [
                "arn:aws:codebuild:*:398188212409:project/*"
            ]
        },
        {
            "Sid": "VisualEditor5",
            "Effect": "Allow",
            "Action": [
                "codecommit:List*",
                "codecommit:Get*",
                "codecommit:GitPull",
                "codecommit:UploadArchive",
                "codecommit:CancelUploadArchive"
            ],
            "Resource": "arn:aws:codecommit:*:398188212409:*"
        },
        {
            "Sid": "VisualEditor6",
            "Effect": "Allow",
            "Action": [
                "codepipeline:GetPipeline"
            ],
            "Resource": "arn:aws:codepipeline:*:398188212409:*"
        }
    ]
}