<br>

# Impact Assessment

<br>

The team does not have a standard workload.  Solutions that it designs, develops, tests, etc., will be delivered to 
clients/colleagues. This brief assessment considers a hypothetical, but partially representative, scenario.

<br>

```{contents}
:local:
```

<br>

## Scenario


### Project in focus

The design, development, and delivery of a machine learning product that will forecast particulate matter levels for a small geographic area. The client will use it to dynamically control traffic flow into the area.

<br>

### Assets stored within the cloud platform

In this case, the assets are **(a)** raw data, **(b)** processed data, **\(c\)** engineered features, **(d)** image 
containers, and **(e)** developed models & artefacts.

<br>

### Design, development, and resources zones

These are:

* Local mobile workstations<br>
  For developing programs **for** data acquisition, programmatic data delivery to Amazon S3, data processing, features engineering, modelling, infrastructure as code (IAC), etc.

* GitHub & GitHub Actions<br>
  For version control, code analysis, dependencies vulnerability analysis, building & storing container images, and 
  trackable delivery of code assets to Amazon Web Services.

* Amazon Web Services<br>
  For **(a)** secure storage of data, container images, models, and artefacts of models, **(b)** computing resources, and 
  **\(c\)** designing, developing and testing machine learning systems solution architectures based on infrastructure-as-code programs.

<iframe
style="overflow:hidden; width:100%; height:330px; border:none;"
src="../../../../assets/beforehand.html"></iframe>
<figure>
<figcaption>An illustration of a team member's interaction with cloud services</figcaption>
</figure>

<br>

### Plausible Disruptions

The plausible disruptions are:

* Data loss
* Data breach
* Data corruption; loss of integrity.
* Unavailable services/data due to platform malfunction


<br>
<br>


## Considerations & Contingencies vis-à-vis Disruptions

Overall, disruptions will impact project delivery times, and will cost money.  In future, and depending on the context, the 
team will have to consider a mix of financial, operational, legal, and/or regulatory impacts of disruptions.

<br>

### Data Loss / Data Breach

* **Confidentiality:** The team will only store open data, and their derivatives, within the cloud platform.  Therefore, 
confidentiality issues vis-à-vis sensitive or personal data are inapplicable.

* **Recovery:** The back-up routes are **(a)** [AWS Back-up for Amazon S3 (Simple Storage Service)](https://docs.aws.amazon.
com/AmazonS3/latest/userguide/backup-for-s3.html), and **(b)** re-running the project's container images.

<br>

### Data Corruption

* **Recovery:** The back-up routes are **(a)** [AWS Back-up for Amazon S3 (Simple Storage Service)](https://docs.aws.
  amazon.com/AmazonS3/latest/userguide/backup-for-s3.html), and **(b)** re-running the data acquisition, data processing, 
  features engineering, modelling, etc., images.

<br>

### Unavailable Cloud Platform

* **Contingency**: Use a different computing hub to **(a)** retrieve the back-up container images from GitHub Container 
  Registry, and **(b)** run the containers. [Each container image registration is via GitHub Container Registry (GCR) and Amazon Elastic Container Registry (ECR).]


<br>
<br>

<br>
<br>

<br>
<br>

<br>
<br>
