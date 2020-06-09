[Final Project Slides](https://docs.google.com/presentation/d/1zvD-UGyEbN1OazQ2ZLZhiMNwUVC6RImd-o0YFmxDx80/edit?usp=sharing)

# FRED - The Anti-bot CAPTCHA
FRED is a system that utilizes adversarial examples to generate images that will fool machine learning CAPTCHA bots.
## Adversarial Examples
### Attacks
#### [FGSM](https://github.com/ECS153/final-project-the-flintstones/blob/d1ff7705e5fad1a5336fd75aa055eb03940dd409/scripts/Attacks.py#L12)
This is one possible attack algorithm that we can use to generate adversarial examples. Perturbations are generated using the gradients of loss with respect to the input image scaled by an epsilon value.

#### [MI-FGSM](https://github.com/ECS153/final-project-the-flintstones/blob/d1ff7705e5fad1a5336fd75aa055eb03940dd409/scripts/Attacks.py#L17)
This is the momentum-based variant of the FGSM. This algorithm yields our best results for generating adversarial examples. Gradients are accumulated in each iteration with a decay factor and the adversarial example is perturbed toward the sign of t-th gradient with a step size of alpha (epsilon / T) in each iteration.

#### [L<sub>0</sub> Attack](https://github.com/ECS153/final-project-the-flintstones/tree/master/carlini_l0_attempt)
Begins by distorting many pixels and gradually modifies less and less pixels while testing the modifications until a minimal point is reached with a significant confidence level. The directory shows our progress on attempting to implement the attack.

### Machine Learning Model
The model is a sequential convolutional neural network trained on digital English letters from Chars74K data set. We use this model both for the attack algorithms and our testing bot's prediction on our adversarial examples.  

Accuracy: 0.9667, Loss: 0.0023

## Website/CAPTCHA Matching
We use HTML, CSS, and Javascript to load a webpage with our CAPTCHA to simulate a use case of our project: a website sign up page.

#### [Wrap CAPTCHA Within HTML](https://github.com/ECS153/final-project-the-flintstones/blob/08d89e5c49e068c1d89ddec9c1bd0f58846ca680/project/fred.html#L30)
#### [Call captchaGen() onload](https://github.com/ECS153/final-project-the-flintstones/blob/08d89e5c49e068c1d89ddec9c1bd0f58846ca680/project/fred.html#L11)

#### [CAPTCHA Generation](https://github.com/ECS153/final-project-the-flintstones/blob/08d89e5c49e068c1d89ddec9c1bd0f58846ca680/project/button.js#L46)
####
Call function [randomizeCap](https://github.com/ECS153/final-project-the-flintstones/blob/08d89e5c49e068c1d89ddec9c1bd0f58846ca680/project/button.js#L104)
to generate a randomly ordered set of integers that will determine the order of the letters.
#### [Correct Input](https://github.com/ECS153/final-project-the-flintstones/blob/08d89e5c49e068c1d89ddec9c1bd0f58846ca680/project/button.js#L65)
Parse the randomized order of the returned array and simultaneously display the CAPTCHA in that order while recording the correctInput.
#### [Matching User Input](https://github.com/ECS153/final-project-the-flintstones/blob/08d89e5c49e068c1d89ddec9c1bd0f58846ca680/project/button.js#L7)
User is given three tries to correctly input the CAPTCHA before being redirected to either a FAIL or SUCCESS page. Each incorrect try also rearranges the order of the CAPTCHA.


## General Use
### Generating Adversarial Examples
Running `python generate_examples.py` will perform an attack on 5 random images from the dataset and outputs the model's prediction on the images as well as the images themselves. Line 26 of the file must be changed to specify what Attack you want to be used. The [model](https://drive.google.com/file/d/1mIr5lVTdYXoVJkhu0P8jNjAMYQCFsHGS/view?usp=sharing) and [dataset](https://drive.google.com/file/d/1goaA1kAqefS9tELiQdpNDW2D2kRlFWK9/view?usp=sharing) files must be in the same directory.

To use `Attacks.py` import it into the script you are writing.
