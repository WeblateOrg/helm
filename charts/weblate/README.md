# weblate

![Version: 0.5.24](https://img.shields.io/badge/Version-0.5.24-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 5.12.2.3](https://img.shields.io/badge/AppVersion-5.12.2.3-informational?style=flat-square)

Weblate is a free web-based translation management system.

**Homepage:** <https://weblate.org/>

## Maintainers

| Name | Email | Url |
| ---- | ------ | --- |
| tarioch | <patrick@ch.tario.org> |  |
| nijel | <michal@weblate.org> |  |

## TL;DR;

```console
$ helm repo add weblate https://helm.weblate.org
$ helm install my-release weblate/weblate
```

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://charts.bitnami.com/bitnami | postgresql | 16.7.15 |
| https://charts.bitnami.com/bitnami | redis | 21.1.11 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| adminEmail | string | `""` | Email of Admin Account |
| adminPassword | string | `""` | Password of Admin Account |
| adminUser | string | `""` | Name of Admin Account |
| affinity | object | `{}` |  |
| allowedHosts | string | `"*"` | Hosts that are allowed to connect |
| caCertSecretName | string | `""` | Secret containing a custom CA cert bundle to be mounted. See https://docs.weblate.org/en/latest/admin/install.html?highlight=certificates#using-custom-certificate-authority |
| caCertSubPath | string | `""` | Name of the CA cert bundle in the secret, e.g. ca-certificates.crt or ca-bundle.crt |
| configOverride | string | `""` | Config override. See https://docs.weblate.org/en/latest/admin/install/docker.html#custom-configuration-files |
| containerSecurityContext.enabled | bool | `false` |  |
| debug | string | `"0"` | Enable debugging |
| defaultFromEmail | string | `""` | From email for outgoing emails |
| emailHost | string | `"chart-example.local"` | Host for sending emails |
| emailPassword | string | `""` | Password for sending emails |
| emailPort | int | `587` | Port for sending emails |
| emailSSL | bool | `false` | Use SSL when sending emails |
| emailTLS | bool | `true` | Use TLS when sending emails |
| emailUser | string | `""` | User name for sending emails |
| existingSecret | string | `""` | Name of existing secret, Make sure it contains the keys postgresql-user, postgresql-password, redis-password, email-user, email-password, admin-user, admin-password Also note to set the existingSecret values for the Redis and Postgresql subcharts |
| externalSecretName | string | `""` | An external secret, in the same namespace, that will be use to set additional (environment) configs. |
| extraConfig | object | `{}` | Additional (environment) configs. Values will be evaluated as templates. See https://docs.weblate.org/en/latest/admin/install/docker.html#docker-environment |
| extraSecretConfig | object | `{}` | Same as `extraConfig`, but created as secrets. Values will be evaluated as Helm templates |
| extraVolumeMounts | list | `[]` | Additional volume mounts to be added to the container. Values will be evaluated as templates. Normally used with `extraVolumes` |
| extraVolumes | list | `[]` | Additional volumes to be added to the deployment. Values will be evaluated as templates. Requires setting `extraVolumeMounts` |
| fullnameOverride | string | `""` |  |
| image.pullPolicy | string | `"IfNotPresent"` |  |
| image.repository | string | `"weblate/weblate"` |  |
| image.tag | string | `"5.12.2.3@sha256:322a0986a986f3bd1d6a30c6ec7ec29c64ff32bf0a015db19a892a27b41fc037"` |  |
| imagePullSecrets | list | `[]` |  |
| ingress.annotations | object | `{}` |  |
| ingress.enabled | bool | `false` |  |
| ingress.hosts[0].host | string | `"chart-example.local"` |  |
| ingress.hosts[0].paths[0].path | string | `"/"` |  |
| ingress.hosts[0].paths[0].pathType | string | `"Prefix"` |  |
| ingress.ingressClassName | string | `""` |  |
| ingress.tls | list | `[]` |  |
| initContainers | list | `[]` | List of init containers to add to the pod. Values will be evaluated as Helm templates |
| labels | object | `{}` | custom labels |
| livenessProbe.failureThreshold | int | `10` |  |
| livenessProbe.initialDelaySeconds | int | `300` |  |
| livenessProbe.periodSeconds | int | `30` |  |
| livenessProbe.successThreshold | int | `1` |  |
| livenessProbe.timeoutSeconds | int | `5` |  |
| nameOverride | string | `""` |  |
| nodeSelector | object | `{}` |  |
| persistence.accessMode | string | `"ReadWriteOnce"` |  |
| persistence.enabled | bool | `true` |  |
| persistence.existingClaim | string | `""` | Use an existing volume claim |
| persistence.filestore_dir | string | `"/app/data"` |  |
| persistence.size | string | `"10Gi"` |  |
| podAnnotations | object | `{}` |  |
| podLabels | object | `{}` |  |
| podSecurityContext.enabled | bool | `true` |  |
| podSecurityContext.fsGroup | int | `1000` |  |
| postgresql.auth.database | string | `"weblate"` |  |
| postgresql.auth.enablePostgresUser | bool | `true` |  |
| postgresql.auth.existingSecret | string | `""` |  |
| postgresql.auth.postgresPassword | string | `"weblate"` |  |
| postgresql.auth.secretKeys.userPasswordKey | string | `"postgresql-password"` |  |
| postgresql.auth.userName | string | `""` |  |
| postgresql.enabled | bool | `true` |  |
| postgresql.postgresqlHost | string | `None` | External postgres database endpoint, to be used if `postgresql.enabled == false` |
| postgresql.service.ports.postgresql | int | `5432` |  |
| readinessProbe.failureThreshold | int | `2` |  |
| readinessProbe.initialDelaySeconds | int | `60` |  |
| readinessProbe.periodSeconds | int | `30` |  |
| readinessProbe.successThreshold | int | `1` |  |
| readinessProbe.timeoutSeconds | int | `5` |  |
| redis.architecture | string | `"standalone"` |  |
| redis.auth.enabled | bool | `true` |  |
| redis.auth.existingSecret | string | `""` |  |
| redis.auth.existingSecretPasswordKey | string | `"redis-password"` |  |
| redis.auth.password | string | `"weblate"` |  |
| redis.db | int | `1` |  |
| redis.enabled | bool | `true` |  |
| redis.redisHost | string | `None` | External redis database endpoint, to be used if `redis.enabled == false` |
| replicaCount | int | `1` |  |
| resources | object | `{}` |  |
| secretAnnotations | object | `{}` |  |
| serverEmail | string | `""` | Sender for outgoing emails |
| service.annotations | object | `{}` |  |
| service.port | int | `80` |  |
| service.type | string | `"ClusterIP"` |  |
| serviceAccount.create | bool | `true` |  |
| serviceAccount.name | string | `nil` |  |
| sidecars | list | `[]` | List of additional containers to add to the pod. Values will be evaluated as Helm templates |
| siteDomain | string | `"chart-example.local"` | Site domain |
| sitePrefix | string | `""` | Site Prefix (ex: /weblate) |
| siteTitle | string | `"Weblate"` |  |
| tolerations | list | `[]` |  |
| updateStrategy | string | `"Recreate"` |  |
