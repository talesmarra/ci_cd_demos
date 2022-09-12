# CI/CD example repository

This repository aims to show up some basic CI/CD. 

To do so, we'll use [GitHub Actions](https://docs.github.com/en/actions/),
a tool that allows to implement workflows for different branches and with different jobs;

For those unfamiliar with the terms, we'll talk a little bit about them and their practical implications:
 
## CI

CI stands for continuous integration, which means the continual improvement of the code base, with appropriate 
**TESTING** and integration to a shared source;

Regarding test automatisation, using Actions allows you to setup the launching of lint and tests
for each developer branch, making sure that the integrity of that codebase is maintained. 

To be able to launch those tests, you'll need the proper base. 

Quickly saying, a basic python project structure would look like this:

<img src="https://user-images.githubusercontent.com/46964784/189723386-f79bc032-fb9d-45ed-a5f7-36a8d129031d.png" width="600" height="400" align="center" />

Once this structure is set, you can move to the `.github/workflows/workflow.yml` and see the different steps
involved in launching automated tests on the code base. We prepare the environment by doing installation and eventual
updates to packages; then we check for syntax errors etc. using lint and finally we launch our unit tests with
pytest.

The result you obtain when clicking over the Actions button is like the following:
![ci](https://user-images.githubusercontent.com/46964784/189722255-62ecd6b1-e637-4f6b-ae70-41a6d4820383.png)

## CD 

CD stands for continual delivery/deployment. It means that the deployment to production and to other developers/users
should be automated as well.

This is also possible with GitHub Actions, where you can publish your packages, images etc. when a version is tagged for
instance.

The example for this is in `.github/workflows/deploy.yml`, where we only stored the generated wheel as an artifact in Git,
but you can deploy it to any Artifactory you desire;

The end result can be seen below:
![deploy_workflow](https://user-images.githubusercontent.com/46964784/189721742-9ed1738f-803b-4c24-b53a-1b230e87949e.png)
