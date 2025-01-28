# LFRic-Atmosphere-Training

This repository hosts the materials developed to support self-learning of the Momentum LFRic Atmosphere. This training is designed to provide an introductory level training for the LFRic Atmospheric model, as well as its associated workflows. The training material includes modules on various topics such as the motivation behind the development of LFRic, an overview of the model, development working practices, visualisation of mesh data, LFRic based Science Configurations, and practical exercises for hands-on learning.

The training is structured to cater to users with different levels of expertise, from beginners to advanced users. It covers essential aspects like understanding model input and output files, navigating code repositories, and running model configurations. The goal is to make the training accessible and beneficial for all Momentum users, ensuring they can effectively use the LFRic Atmosphere model.

The LFRic Atmosphere self-learning training can be found at <https://metoffice.github.io/LFRic-Atmosphere-Training>

## Contributing & Development

The preferred way to contribute to LFRic-Atmosphere-Training is to fork the main repository, then submit a "pull request" (PR). When updating this training material, aim for clear and easy-to-understand contnent. Please keep in mind that this intended for an introductory level training.

To [create a fork](https://github.com/MetOffice/LFRic-Atmosphere-Training/fork)
under your own account. Use the following commands to clone the correct repository and create a `latest` branch pointing to the [`main` branch in this repository](https://github.com/MetOffice/LFRic-Atmosphere-Training/tree/main).

When creating new branches use the `latest` branch as the parent branch unless a feature branch exists.

```bash

# Clone your forked repository into a LFRic-Atmosphere-Training folder
git clone https://github.com/<GITHUB-USERNAME>/LFRic-Atmosphere-Training.git

cd LFRic-Atmosphere-Training

# Add the MetOffice LFRic-Atmosphere-Training repository as an upstream remote
git remote add upstream https://github.com/MetOffice/LFRic-Atmosphere-Training.git

# This gets all the updates from all your remotes (your fork and the central repository)
git fetch --all

# This creates a new branch called latest which follows upstream/main and checks it out.
git checkout upstream/main -b latest

# And to prevent accidentally pushing to upstream/main...
git remote set-url --push upstream no_push

# And to prevent pushing your origin/main branch to unwanted places...
git branch -D main
```

### Development Environment

Conda is the recommended Python package manager for setting up the development environment, to build the trainning pages.

In order to install the standard development environment run the following command:

```bash
conda env create --file environment.yml
```

Now activate the development environment with Conda:

```bash
conda activate lfric-atmosphere-training
```

Once the development environment is set up you are ready to build the training materials.

### Building Training Materials

The training materials are based on [Sphinx](https://www.sphinx-doc.org) and can be built using the provided Makefile on any desired target format. However, we aim to display the content as HTML pages, and any contributions should ensure these are produced correctly.

To build the LFRic Atmosphere training materials in HTML format run the following command:

```bash
make html
```

That concludes the process! You’ll find the generated HTML files within the “build” folder.

### Pull Request (PR) Process

1. Create a well-documented PR with a description of changes.
1. Request reviews from the the [Momentum Partnership Team](mailto:Momentum_Partnership@metoffice.gov.uk) or other maintainers.
1. Respond to feedback and make changes if required.
1. Wait for approval and merging.

## Contacts

If you want to get in contact with us, or have any questions, don't hesitate to email the [Momentum Partnership Team](mailto:Momentum_Partnership@metoffice.gov.uk).
