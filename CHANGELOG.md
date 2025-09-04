## 0.5.25

[FEATURE] Add revisionHistoryLimit [#619](https://github.com/WeblateOrg/helm/pull/619)
[BUGFIX] Use bitnami images from docker.io/bitnamilegacy for dependencies due to bitnami deprecating their public catalog. See bitnami/charts#35164

## 0.5.24

[FEATURE] Add `timeoutSeconds` and `successThreshold` for **livenessProbe** and **readinessProbe** [#583](https://github.com/WeblateOrg/helm/issues/583)

## 0.5.23

[BUGFIX] Only trigger a reload of the pod, if the pod template change or the configuration changes [#557](https://github.com/WeblateOrg/helm/pull/557)

## 0.5.22

[FEATURE] Add podLabels [#554](https://github.com/WeblateOrg/helm/pull/554)
[BUGFIX] Remove unnecessary newlines in rendered chart [#556](https://github.com/WeblateOrg/helm/pull/556)

## 0.5.20

[BUGFIX] Remove `common.tplvalues.render` function [#502](https://github.com/WeblateOrg/helm/issues/502)

## 0.5.18

[BUGFIX] Change value `emailSSL` to `false` [#143](https://github.com/WeblateOrg/helm/issues/143)

## 0.5.16

[BUGFIX] Fix service name for Redis and Postgres [#327](https://github.com/WeblateOrg/helm/issues/327)
