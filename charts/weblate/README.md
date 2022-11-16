# weblate

![Version: 1.1.0](https://img.shields.io/badge/Version-1.1.0-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 4.14.2](https://img.shields.io/badge/AppVersion-4.14.2-informational?style=flat-square)

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
| https://charts.bitnami.com/bitnami | postgresql | 12.1.2 |
| https://charts.bitnami.com/bitnami | redis | 17.3.11 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| fullnameOverride | string | `""` |  |
| image.pullPolicy | string | `"IfNotPresent"` |  |
| image.pullSecrets | list | `[]` |  |
| image.repository | string | `"weblate/weblate"` |  |
| image.tag | string | `"4.14.2-1"` |  |
| ingress.annotations | object | `{}` |  |
| ingress.enabled | bool | `false` |  |
| ingress.hosts[0].host | string | `"chart-example.local"` |  |
| ingress.hosts[0].paths[0].path | string | `"/"` |  |
| ingress.hosts[0].paths[0].pathType | string | `"Prefix"` |  |
| ingress.ingressClassName | string | `""` |  |
| ingress.tls | list | `[]` |  |
| labels | object | `{}` |  |
| nameOverride | string | `""` |  |
| persistence.accessMode | string | `"ReadWriteOnce"` |  |
| persistence.enabled | bool | `true` |  |
| persistence.existingClaim | string | `""` | Use an existing volume claim |
| persistence.filestore_dir | string | `"/app/data"` |  |
| persistence.size | string | `"10Gi"` |  |
| postgresql.auth.database | string | `"weblate"` |  |
| postgresql.enabled | bool | `true` |  |
| redis.architecture | string | `"standalone"` |  |
| redis.auth.enabled | bool | `true` |  |
| redis.db | int | `1` |  |
| redis.enabled | bool | `true` |  |
| service.annotations | string | `nil` |  |
| service.port | int | `80` |  |
| service.type | string | `"ClusterIP"` |  |
| serviceAccount.enabled | bool | `true` |  |
| serviceAccount.name | string | `nil` |  |
| weblate.affinity | object | `{}` |  |
| weblate.allowedHosts | string | `"*"` |  |
| weblate.caCertSecretName | string | `""` |  |
| weblate.caCertSubPath | string | `""` |  |
| weblate.configOverride | string | `""` |  |
| weblate.containerSecurityContext.enabled | bool | `false` |  |
| weblate.debug | string | `"0"` |  |
| weblate.defaultUser.email | string | `""` |  |
| weblate.defaultUser.existingSecret | object | `{}` |  |
| weblate.defaultUser.password | string | `""` |  |
| weblate.defaultUser.username | string | `"admin"` |  |
| weblate.email.auth.existingSecret | object | `{}` |  |
| weblate.email.auth.password | string | `""` |  |
| weblate.email.auth.user | string | `""` |  |
| weblate.email.defaultFromEmail | string | `""` |  |
| weblate.email.host | string | `""` |  |
| weblate.email.port | int | `587` |  |
| weblate.email.serverEmail | string | `""` |  |
| weblate.email.ssl | bool | `false` |  |
| weblate.email.tls | bool | `true` |  |
| weblate.externalPostgres | object | `{}` |  |
| weblate.externalRedis | object | `{}` |  |
| weblate.externalSecretName | string | `""` |  |
| weblate.extraConfig | object | `{}` |  |
| weblate.extraConfigSecrets | list | `[]` |  |
| weblate.extraSecretConfig | object | `{}` |  |
| weblate.nodeSelector | object | `{}` |  |
| weblate.podSecurityContext.enabled | bool | `true` |  |
| weblate.podSecurityContext.fsGroup | int | `1000` |  |
| weblate.replicaCount | int | `1` |  |
| weblate.resources | object | `{}` |  |
| weblate.siteDomain | string | `"chart-example.local"` |  |
| weblate.siteTitle | string | `"Weblate"` |  |
| weblate.tolerations | list | `[]` |  |
| weblate.updateStrategy | string | `"Recreate"` |  |
