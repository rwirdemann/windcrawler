// Import the [pulumi/aws](https://pulumi.io/reference/pkg/nodejs/@pulumi/aws/index.html) package
const pulumi = require("@pulumi/pulumi");
const aws = require("@pulumi/aws");
const awsx = require("@pulumi/awsx");

const policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": "sts:AssumeRole",
            "Principal": {
                "Service": "lambda.amazonaws.com",
            },
            "Effect": "Allow",
            "Sid": "",
        },
    ],
};

const role = new aws.iam.Role("precompiled-lambda-role", {
    assumeRolePolicy: JSON.stringify(policy),
});

const pythonLambda = new aws.lambda.Function("windcrawler", {
    runtime: aws.lambda.Python3d6Runtime,
    code: new pulumi.asset.AssetArchive({
        ".": new pulumi.asset.FileArchive("../."),
    }),
    timeout: 5,
    handler: "handler.handler",
    role: role.arn
});

const api = new awsx.apigateway.API("windcrawler", {
    routes: [{
        path: "/", 
        method: "GET", 
        eventHandler: pythonLambda }],
})

exports.url = api.url;