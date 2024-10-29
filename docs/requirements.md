# **psCompose Product Requirements Document (PRD)**

## **Objective**

psCompose is a web-based UI for perfSONAR administrators to define and publish pSConfig templates, which automate tests executed by test nodes, and provides topology information to various services, such as Grafana and pScheduler.

## **Problem Statement**

The current version of PWA is built on the MEAN stack (MongoDB, Express, Angular, and Node.js), a technology set that is not used in any other perfSONAR projects, making PWA somewhat of an outlier. Additionally, the development team lacks familiarity with these technologies, complicating collaboration efforts. The existing codebase has grown so complex that bug fixes are challenging, leading to unreliable performance in production environments.

## **Anticipated Users**

Users that need to create, modify, or access pSConfig templates

## **Test User Contacts**

perfSONAR dev team

## **Decision Makers**

Andy Lake

## **Definition of Terms**:
[https://docs.perfsonar.net/psconfig_templates_intro.html](https://docs.perfsonar.net/psconfig_templates_intro.html)


        Address:	A collection of properties that act as the unit of input to a task.


        Agent:	Software that reads one or more pSConfig templates and uses the information to perform a specific function. Currently *pscheduler-agent* and *maddash-agent*.


        Archive:	An optional component of the template that tells agents where the results of the described tasks are to be stored.


        Group:	A description of how to combine addresses when building the list of tasks.


        Schedule:	An optional component of the template that tells agents how often to run a task.


        Task:	A job to do consisting of a test to be carried out, scheduling information and other options.


        Template:	A description of the task topology in a machine readable format (JSON).


        Test:	Defines the parameters of the job to be carried out by the task.


        Topology:	How the tasks are interrelated and arranged. Currently *mesh*, *disjoint*, or *list*.


## **v1.0 Requirements**

### **Functional Requirements (Must haves)**

* Reusability
    * Groups, Tests, and Archives must be reusable in multiple templates without the need for duplicate data entry
* Publishing
    * Templates must be accessible from customizable URLs
* User Administration and Authentication
    * The main admin must be able to add other users as either admins or normal users
    * All users must use a HTTP Basic Auth (username/password) to login
    * User will be assigned either an admin role or a regular user role
* Importing
    * Users must be able to accurately import existing pSConfig templates from a URL, file, or raw JSON
* Test Creation
    * Tests must support *mesh*, *disjoint *and *list* group types
    * Support any test that pScheduler supports, such as throughput, ping, one-way latency and traceroute tests. This data will be retrieved from the pScheduler API
    * Users must be able to set optional test parameters
* Support for Contexts
    * Users should be able to define context objects which allow certain user-specified changes to the execution context prior to execution of that tool running a test
    * [https://docs.perfsonar.net/psconfig_templates_advanced.html#using-contexts](https://docs.perfsonar.net/psconfig_templates_advanced.html#using-contexts)
* Schedule Interval
    * Users must be able to specify the interval between task runs in either seconds or by using a cron-style interval
* Support Archivers
    * Support any archiver that pScheduler supports. This data will be retrieved from the pScheduler API
* Auto Templating
    * Users must be able to generate an *auto template* (JSON) which aggregates all tests defined in various templates for a specific host
    * Concept here is that we can retrieve all applicable tests for a specific host, even if the tests are defined in separate perfSONAR installations
* Variable Substitutions
    * Support for template variables in the template JSON should be provided. 
    * Various template variables are defined here - [https://docs.perfsonar.net/psconfig_templates_vars.html](https://docs.perfsonar.net/psconfig_templates_vars.html) 
* Common Display Options
    * There are options common to all tasks that are used to inform how the tasks are displayed in things like Grafana. Specifically a task reference section can have a display-task-name and display-task-group. They are not in the schema but they are important to current agents, so we should make it easy to set these.
    * Example JSON: [https://github.com/perfsonar/psconfig/blob/master/psconfig/perfsonar-psconfig/doc/skeleton.json#L94-L97](https://github.com/perfsonar/psconfig/blob/master/psconfig/perfsonar-psconfig/doc/skeleton.json#L94-L97) 
* Autocompletion
    * This is necessary to prevent typos/errors. As you start typing, it narrows the selection based upon what is already available - using lookup service info
    * This will be helpful when adding hosts
* User Options
    * Users should have the ability to see their most recently edited items, such as recently edited host groups and templates
    * Users should be able to mark items as favorites, such as favorite host groups

### **Functional Requirements (Nice to haves)**

* Dynamic Groups
    * Users must be able to enter host selection criteria to be evaluated at runtime
* Editing Privilege
    * Admins must be able to grant editing privileges for specific archives, tests, groups, and templates to specific users
* Setting Advanced options
    * [https://docs.perfsonar.net/psconfig_templates_advanced.html](https://docs.perfsonar.net/psconfig_templates_advanced.html)
    * These include advanced addresses, groups and hosts options, sharing address properties with hosts, and including external files
* Advanced filtering of hosts
    * When adding new hosts, users should have the ability to search through the simple lookup service to filter out stuff via advanced optionssuch as give me all hosts with XYZ criteria etc

### **Technical Requirements:**

* API
    * Users must be able to create/update/retrieve Templates, Hosts, Host Groups, Tests and Tasks via a REST API
* Authentication
    * We shall be using HTTP Basic Auth for authentication
* Database
    * The supporting database will be PostgreSQL
* Validation
    * Generated templates must use the [pSConfig Schema](https://raw.githubusercontent.com/perfsonar/psconfig/master/psconfig/perfsonar-psconfig/doc/psconfig-schema.json)
    * Valid schema can be found here - [https://raw.githubusercontent.com/perfsonar/psconfig/master/psconfig/perfsonar-psconfig/doc/psconfig-schema.json](https://raw.githubusercontent.com/perfsonar/psconfig/master/psconfig/perfsonar-psconfig/doc/psconfig-schema.json)
* Deployment
    * The final product must be available as Docker images, RPMs and deb packages.
    * Use Unibuild to support multiple packages by configuring the repository in a particular format with unibuild-order
        * [https://github.com/perfsonar/unibuild](https://github.com/perfsonar/unibuild)
