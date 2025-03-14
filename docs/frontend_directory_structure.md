# psCompose Frontend Directory Structure Notes

## Motivation

We intended to create a scheme that leverages "standard HTTP" as well as possible,
while also allowing for reuse.

There are two main sections for the application:
  -  `/templates/` which contains reusable HTML templates of discreen UI sections
  -  `/app/` which contains the UI proper

## Concepts

We indended to organize files so that they would be as intelligible as possible,
in the context of a text editor, as well as in a browser.

We selected URLs such as `/tasks/` for the tasks section of the application.

The `/tasks/` directory also contains `tasks.html`. `tasks.html` is then
symbolically linked to the name `index.html` so that it can be accessed
in a browser as `/tasks/`. This was intended to provide an easy editing 
experience as well as a more modern-looking url.

## Layout notes

### Templates

```
pscompose/frontend/templates/
    flyout_menu.html
    editing_form.html
    progress_bar.html
    top_nav.html
    left_nav.html
    ... other stuff
```

### Components

```
pscompose/frontend/components/
    ... all web components
```

### Application

```
pscompose/frontend/app/
    index.html
    templates/
        templates.html
        index.html -> ./templates.html
    tasks/
        tasks.html
        index.html -> ./tasks.html
    contexts/
        index.html
    tests/
        index.html
    ... other datatypes
    wizard/
        hosts/
            wizard_hosts.html
            index.html -> wizard_hosts.html
        groups/
            index.html
        ... etc
```