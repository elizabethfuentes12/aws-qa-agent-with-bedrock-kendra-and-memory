# RAG on AWS usign Amazon Bedrock, Amazon Kendra, Amazon Lambda Function and Amazon DynamoDB

🇻🇪🇨🇱 [Dev.to](https://dev.to/elizabethfuentes12) [Linkedin](https://www.linkedin.com/in/lizfue/) [GitHub](https://github.com/elizabethfuentes12/) [Twitter](https://twitter.com/elizabethfue12) [Instagram](https://www.instagram.com/elifue.tech) [Youtube](https://www.youtube.com/channel/UCr0Gnc-t30m4xyrvsQpNp2Q)
[Linktr](https://linktr.ee/elizabethfuentesleone)

---

In this repository you will find a use cases of RAG on AWS using [CDK](https://docs.aws.amazon.com/cdk/v2/guide/home.html). 

Additionally,  you will find a notebook where you can run the agent localy.

Multilingual (limited to the LLM you use) agent with memory capable of following a more fluid conversation (learn more about using memories with agents [here](https://community.aws/posts/working-with-your-live-data-using-langchain)) to query the re:invent 2023 agenda by session ID or by description or general information, it also recommend a list of sessions according to your input. 

![Digrama parte 1](/imagenes/image_01.png)

✅ **AWS Level**: Intermediate - 200   

**Prerequisites:**

- [AWS Account](https://aws.amazon.com/resources/create-account/?sc_channel=el&sc_campaign=datamlwave&sc_content=cicdcfnaws&sc_geo=mult&sc_country=mult&sc_outcome=acq) 
-  [Foundational knowledge of Python](https://catalog.us-east-1.prod.workshops.aws/workshops/3d705026-9edc-40e8-b353-bdabb116c89c/) 

💰 **Cost To Complete**: 
- [Amazon Bedrock Pricing](https://aws.amazon.com/bedrock/pricing/)
- [Amazon Lambda Pricing](https://aws.amazon.com/lambda/pricing/)
- [Amazon DynamoDB Pricing](https://aws.amazon.com/dynamodb/pricing/)
- [Amazon Kendra Pricing](https://aws.amazon.com/kendra/pricing/)

## Let's build!

✅ **Go to**: 

```
cd re-invent-agent
```

✅ **Create The Virtual Environment**: by following the steps in the [README](/re-invent-agent/README.md)

```
python3 -m venv .venv
```

```
source .venv/bin/activate
```
for windows: 

```
.venv\Scripts\activate.bat
```

✅ **Install The Requirements**:

```
pip install -r requirements.txt
```

✅ **Synthesize The Cloudformation Template With The Following Command**:

```
cdk synth
```

✅🚀 **The Deployment**:

```
cdk deploy
```

✅ **Configuration:** 

When the stack is deployed, go to the Amazon Kendra console and Choose the new Index and then **Sync Now** 

![Digrama parte 1](/imagenes/image_06.png)

This will populate the Index with the re-invent [agenda data](/re-invent-agent/agenda_reinvent_2023) that the CDK stack loaded into the S3 bucket it created. ⏳ It will take a while, be patient.


✅ **Test The Agent Locally:** [Here](re-invent-agent.ipynb)

✅ **Test The Agent:**

- [Testing Lambda Functions In The Console](https://docs.aws.amazon.com/lambda/latest/dg/testing-functions.html):

Go to the [Lamnda Function console](https://console.aws.amazon.com/lambda/home#/functions), serarch and choose the lambda function that starts with the name `ReInventAgentStack-Fnagent`

![Digrama parte 1](/imagenes/image_03.png)

Choose the Test tab.

![Digrama parte 1](/imagenes/image_05.png)

Under Test event, choose Create new event, in **Event Json** create a event like this: 

```
{
  "prompt": "I'm looking for a session about generative ai",
  "session_id": "1"
}
```

![Digrama parte 1](/imagenes/image_04.png)


Saved event and **Test**. 

Check the response when finished. 

- [Testing Lambda Functions With Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda/client/invoke.html):

In this [notebook](/test_lambda_function.ipynb) you can find the code to test locally.

> Play with the agent and improve the prompt, remember that he has memory storage and you can have a fluid conversation with it.


----

## 🚨 Did you like this blog? 👩🏻‍💻 Do you have comments?🎤 tell me everything [here](https://www.pulse.aws/survey/6V3IYE9H)

----

## ¡Gracias!

🇻🇪🇨🇱 [Dev.to](https://dev.to/elizabethfuentes12) [Linkedin](https://www.linkedin.com/in/lizfue/) [GitHub](https://github.com/elizabethfuentes12/) [Twitter](https://twitter.com/elizabethfue12) [Instagram](https://www.instagram.com/elifue.tech) [Youtube](https://www.youtube.com/channel/UCr0Gnc-t30m4xyrvsQpNp2Q)
[Linktr](https://linktr.ee/elizabethfuentesleone)

---

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.


