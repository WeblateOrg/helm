# weblate

![Version: 0.4.17](https://img.shields.io/badge/Version-0.4.17-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 4.14.1](https://img.shields.io/badge/AppVersion-4.14.1-informational?style=flat-square)

Weblate is a free web-based translation management system.

**Homepage:** <https://weblate.org/>

## Maintainers

| Name    | Email                  | Url |
| ------- | ---------------------- | --- |
| tarioch | <patrick@ch.tario.org> |     |
| nijel   | <michal@weblate.org>   |     |

## TL;DR;

```console
$ helm repo add weblate https://helm.weblate.org
$ helm install my-release weblate/weblate
```

## Requirements

| Repository                         | Name       | Version |
| ---------------------------------- | ---------- | ------- |
| https://charts.bitnami.com/bitnami | postgresql | 11.9.1  |
| https://charts.bitnami.com/bitnami | redis      | 17.3.1  |

## Migrations

See [migration.md](migration.md)

<!--
Parameters generated using bitnami-labs/readme-generator-for-helm
https://github.com/bitnami-labs/readme-generator-for-helm
-->

## Parameters

### Global Settings

| Name                     | Description                                                                    | Value             |
| ------------------------ | ------------------------------------------------------------------------------ | ----------------- |
| `image.repository`       | Weblate image                                                                  | `weblate/weblate` |
| `image.tag`              | Weblate image tag                                                              | `4.14.1-1`        |
| `image.pullPolicy`       | Container image pull policy                                                    | `IfNotPresent`    |
| `image.pullSecrets`      | Container image pull secrets                                                   | `[]`              |
| `nameOverride`           |                                                                                | `""`              |
| `fullnameOverride`       |                                                                                | `""`              |
| `labels`                 | Common labels                                                                  | `{}`              |
| `serviceAccount.enabled` | Enable creating a service account                                              | `true`            |
| `serviceAccount.name`    | Service account name (if not set, it is generated using the fullname template) | `nil`             |


### Weblate

| Name                                                      | Description                                                                                                                                                                  | Value                 |
| --------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------- |
| `weblate.siteTitle`                                       | Weblate site title                                                                                                                                                           | `Weblate`             |
| `weblate.siteDomain`                                      | Weblate site domain                                                                                                                                                          | `chart-example.local` |
| `weblate.replicaCount`                                    | Deployment replica count                                                                                                                                                     | `1`                   |
| `weblate.updateStrategy`                                  | Deployment update strategy                                                                                                                                                   | `Recreate`            |
| `weblate.defaultUser.username`                            | Default admin username                                                                                                                                                       | `admin`               |
| `weblate.defaultUser.password`                            | Default admin password (leave empty to generate a random password)                                                                                                           | `""`                  |
| `weblate.defaultUser.email`                               | Default admin email                                                                                                                                                          | `""`                  |
| `weblate.email.host`                                      | SMTP server host                                                                                                                                                             | `""`                  |
| `weblate.email.port`                                      | SMTP server port                                                                                                                                                             | `587`                 |
| `weblate.email.tls`                                       | SMTP enable TLS (do not turn on when weblate.email.ssl is on)                                                                                                                | `true`                |
| `weblate.email.ssl`                                       | SMTP enable SSL (do not turn on when weblate.email.tls is on)                                                                                                                | `false`               |
| `weblate.email.auth.user`                                 | SMTP username                                                                                                                                                                | `""`                  |
| `weblate.email.auth.password`                             | SMTP password                                                                                                                                                                | `""`                  |
| `weblate.email.serverEmail`                               | Sender email for outgoing error emails                                                                                                                                       | `""`                  |
| `weblate.email.defaultFromEmail`                          | Sender email for outgoing emails                                                                                                                                             | `""`                  |
| `weblate.allowedHosts`                                    | Hosts that are allowed to connect                                                                                                                                            | `*`                   |
| `weblate.debug`                                           | enable debugging                                                                                                                                                             | `0`                   |
| `weblate.nodeSelector`                                    | Node Selector                                                                                                                                                                | `{}`                  |
| `weblate.tolerations`                                     | Tolerations                                                                                                                                                                  | `[]`                  |
| `weblate.affinity`                                        | Affinity                                                                                                                                                                     | `{}`                  |
| `weblate.resources`                                       | Container resource settings                                                                                                                                                  | `{}`                  |
| `weblate.resources.requests.memory`                       | Container resource requests                                                                                                                                                  | `undefined`           |
| `weblate.resources.requests.memory`                       | Container resource requests                                                                                                                                                  | `undefined`           |
| `weblate.resources.limits.cpu`                            | Container resource limits                                                                                                                                                    | `undefined`           |
| `weblate.resources.limits.memory`                         | Container resource limits                                                                                                                                                    | `undefined`           |
| `weblate.caCertSecretName`                                | Secret containing a custom CA cert bundle to be mounted. See https://docs.weblate.org/en/latest/admin/install.html?highlight=certificates#using-custom-certificate-authority | `""`                  |
| `weblate.caCertSubPath`                                   | Name of the CA cert bundle in the secret, e.g. ca-certificates.crt or ca-bundle.crt                                                                                          | `""`                  |
| `weblate.extraConfig`                                     | Additional (environment) configs. Values will be evaluated as templates. See https://docs.weblate.org/en/latest/admin/install/docker.html#docker-environment                 | `{}`                  |
| `weblate.extraSecretConfig`                               | Same as `extraConfig`, but created as secrets. Values will be evaluated as Helm templates                                                                                    | `{}`                  |
| `weblate.externalSecretName`                              | An external secret, in the same namespace, that will be use to set additional (environment) configs.                                                                         | `""`                  |
| `weblate.configOverride`                                  | Config override. See https://docs.weblate.org/en/latest/admin/install/docker.html#custom-configuration-files                                                                 | `""`                  |
| `weblate.podSecurityContext.enabled`                      | Enable Pod Security Context                                                                                                                                                  | `true`                |
| `weblate.podSecurityContext.fsGroup`                      | Set the Pod Security Context fsGroup                                                                                                                                         | `1000`                |
| `weblate.containerSecurityContext.enabled`                | Whether to enable the Container Security Context                                                                                                                             | `false`               |
| `weblate.containerSecurityContext.capabilities`           | Container Security Context capabilities                                                                                                                                      | `{}`                  |
| `weblate.containerSecurityContext.readOnlyRootFilesystem` | Container Security Context enable read only filesystem                                                                                                                       | `undefined`           |
| `weblate.containerSecurityContext.runAsRoot`              | Container Security Context allow running as root                                                                                                                             | `undefined`           |
| `weblate.containerSecurityContext.runAsUser`              | Container Security Context set run as user                                                                                                                                   | `undefined`           |
| `weblate.externalPostgres`                                | External Postgres settings                                                                                                                                                   | `{}`                  |
| `weblate.externalPostgres.host`                           | External Postgres host (only applied if postgresql.enabled is false)                                                                                                         | `undefined`           |
| `weblate.externalPostgres.port`                           | External Postgres port (only applied if postgresql.enabled is false)                                                                                                         | `undefined`           |
| `weblate.externalPostgres.username`                       | External Postgres username (only applied if postgresql.enabled is false)                                                                                                     | `undefined`           |
| `weblate.externalPostgres.password`                       | External Postgres password (only applied if postgresql.enabled is false)                                                                                                     | `undefined`           |
| `weblate.externalPostgres.database`                       | External Postgres database (only applied if postgresql.enabled is false)                                                                                                     | `undefined`           |
| `weblate.externalRedis`                                   | External Redis settings(only applied if redis.enabled is false)                                                                                                              | `{}`                  |
| `weblate.externalRedis.host`                              | External Redis host                                                                                                                                                          | `undefined`           |
| `weblate.externalRedis.port`                              | External Redis port                                                                                                                                                          | `undefined`           |
| `weblate.externalRedis.database`                          | External Redis database                                                                                                                                                      | `undefined`           |
| `weblate.externalRedis.password`                          | External Redis password                                                                                                                                                      | `undefined`           |


### Networking

| Name                       | Description                | Value       |
| -------------------------- | -------------------------- | ----------- |
| `service.type`             | Service type               | `ClusterIP` |
| `service.port`             | Service port               | `80`        |
| `service.annotations`      | Service annotations        | `{}`        |
| `ingress.enabled`          | Enable creating an Ingress | `false`     |
| `ingress.ingressClassName` | Set ingress class name     | `""`        |
| `ingress.annotations`      | Ingress annotations        | `{}`        |
| `ingress.hosts`            | Ingress hosts              | `[]`        |
| `ingress.tls`              | Ingress TLS settings       | `[]`        |


### Persistence

| Name                        | Description                          | Value           |
| --------------------------- | ------------------------------------ | --------------- |
| `persistence.enabled`       | Enable persistent storage            | `true`          |
| `persistence.existingClaim` | Use an existing volume claim         | `""`            |
| `persistence.storageClass`  | Storage class to use for persistency | `undefined`     |
| `persistence.accessMode`    | Volume Claim access mode             | `ReadWriteOnce` |
| `persistence.size`          | Volume Claim size                    | `10Gi`          |
| `persistence.filestore_dir` | Mounting path                        | `/app/data`     |


### Dependencies

| Name         | Description                                                                     | Value |
| ------------ | ------------------------------------------------------------------------------- | ----- |
| `postgresql` | bitnami/postgresql chart values (only deployed when postgresql.enabled is true) | `{}`  |
| `redis`      | bitnami/redis chart values (only deployed when redis.enabled is true)           | `{}`  |

