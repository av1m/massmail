# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)

## [Unreleased]

## [0.1.1] -
### Changed 
* Crypt password users
* Default value for massmail 0 to 1
* If nbMailAttack is > 1, we go directly to smtp (not API).
* ability to change the login password


## [0.1.0] - 15-05-2018
### Added
* Add authentification with Google API --> Don't need to put account on "Allowing less secure apps to access your account"
* Add smtp if client_secret.json don't found
* Add .gitignore (and ignore *.json)
* Change name project 'mailPython' to 'massmail' and upgrade to 2.1
* Add LEGAL
* Add step for installation
* Can add some receivers with add ';'
* SMTP --> Gmail, Yahoo, Hotmail, Outlook, Live, Free, Sfr, Wanadoo, orange
* Use TLS
* Adding a lot of help and information about app

### Changed
* Update pipenv & Python to version 3.7.0

## [0.0.2] - 15-05-2018
### Added
* Add Pipfile

### Changed
* Language change (French --> English)

## [0.0.2] - 15-05-2018
### Added
* add a link to my github page
* formatting the exit button
* added the possibility to put your own email address
* Display ** in the password field
* added the possibility to enter a hotmail / live mail address or gmail

## [0.0.1] - 14-05-2018
### Added
* Establishment of the mail service
* Command Line Interface (CLI)
* add mail mass attack (nb repetition) + default value to 0
* add graphical interface (py -> pyw)
* add button quit
* add confirmation quit the program (IF yes, IF no ...)
* add welcome message + adjust Size & Bold