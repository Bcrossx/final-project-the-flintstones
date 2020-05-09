# Project Proposal
## FRED

### Big Idea
Our project, that we are referring to as “FRED”, is an anti-bot detection project modeled after google captcha. Our primary goal, influenced by Nicholas Carlini’s research we saw in his presentation “Towards Evaluating the Robustness of Neural Networks”, is stopping machine learning bots from overloading a server by using distorted captcha images. For instance we want to make it harder for bots to make troll or spam accounts in a given login or authentication system. By doing this, we hope to provide security for an online server that prevents bots from overloading or creating excessive fake accounts.

### Goal
We plan to build our own anti-bot/anti-spam captcha that will fool captcha solving bots using simple distorted images in a fashion similar to Carlini's research. We believe that by using Carlini’s research idea we will be able to produce a small subset (as we don’t have a lot of resources) of distorted images that will have some negative effect (not sure as to what metrics we should evaluate by as well as what an attainable goal would be) on the ability of a ML bot to successfully solve captchas.
