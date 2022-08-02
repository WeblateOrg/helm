# weblate

![Version: 0.4.13](https://img.shields.io/badge/Version-0.4.13-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 4.14](https://img.shields.io/badge/AppVersion-4.14-informational?style=flat-square)

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
| https://raw.githubusercontent.com/bitnami/charts/defb094c658024e4aa8245622dab202874880cbc/bitnami/ | postgresql | 10.3.14 |
| https://raw.githubusercontent.com/bitnami/charts/defb094c658024e4aa8245622dab202874880cbc/bitnami/ | redis | 12.10.1 |

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
| emailHost | string | `""` | Host for sending emails |
| emailPassword | string | `""` | Password for sending emails |
| emailPort | int | `587` | Port for sending emails |
| emailSSL | bool | `true` | Use SSL when sending emails |
| emailTLS | bool | `true` | Use TLS when sending emails |
| emailUser | string | `""` | User name for sending emails |
| externalSecretName | string | `""` | An external secret, in the same namespace, that will be use to set additionnal (environment) configs. |
| extraConfig | object | `{}` | Additional (environment) configs. Values will be evaluated as templates. See https://docs.weblate.org/en/latest/admin/install/docker.html#docker-environment |
| extraSecretConfig | object | `{}` | Same as `extraConfig`, but created as secrets. Values will be evaluated as Helm templates |
| fullnameOverride | string | `""` |  |
| image.pullPolicy | string | `"IfNotPresent"` |  |
| image.repository | string | `"weblate/weblate"` |  |
| image.tag | string | `"4.14-1"` |  |
| imagePullSecrets | list | `[]` |  |
| ingress.annotations | object | `{}` |  |
| ingress.enabled | bool | `false` |  |
| ingress.hosts[0].host | string | `"chart-example.local"` |  |
| ingress.hosts[0].paths | list | `[]` |  |
| ingress.ingressClassName | string | `""` |  |
| ingress.tls | list | `[]` |  |
| nameOverride | string | `""` |  |
| nodeSelector | object | `{}` |  |
| persistence.accessMode | string | `"ReadWriteOnce"` |  |
| persistence.enabled | bool | `true` |  |
| persistence.existingClaim | string | `""` | Use an existing volume claim |
| persistence.filestore_dir | string | `"/app/data"` |  |
| persistence.size | string | `"10Gi"` |  |
| podSecurityContext.enabled | bool | `true` |  |
| podSecurityContext.fsGroup | int | `1000` |  |
| postgresql.enabled | bool | `true` |  |
| postgresql.postgresqlDatabase | string | `"weblate"` |  |
| postgresql.postgresqlHost | string | `None` | External postgres database endpoint, to be used if `postgresql.enabled == false` |
| postgresql.postgresqlPassword | string | `"weblate"` |  |
| postgresql.postgresqlUsername | string | `"postgres"` | PostgreSQL user should be a superuser to be able to install pg_trgm extension. Alternatively you can install it manually prior starting Weblate. |
| postgresql.service.port | int | `5432` |  |
| redis.cluster.enabled | bool | `false` |  |
| redis.db | int | `1` |  |
| redis.enabled | bool | `true` |  |
| redis.password | string | `"weblate"` |  |
| redis.redisHost | string | `None` | External redis database endpoint, to be used if `redis.enabled == false` |
| replicaCount | int | `1` |  |
| resources | object | `{}` |  |
| serverEmail | string | `""` | Sender for outgoing emails |
| service.annotations | string | `nil` |  |
| service.port | int | `80` |  |
| service.type | string | `"ClusterIP"` |  |
| serviceAccount.create | bool | `true` |  |
| serviceAccount.name | string | `nil` |  |
| siteDomain | string | `"chart-example.local"` | Site domain |
| siteTitle | string | `"Weblate"` |  |
| tolerations | list | `[]` |  |
| updateStrategy | string | `"Recreate"` |  |
