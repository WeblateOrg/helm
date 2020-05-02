weblate
=======
Weblate is a free web-based translation management system.

Current chart version is `0.1.2`

Source code can be found [here](https://weblate.org/)

## Chart Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://charts.bitnami.com/bitnami | postgresql | 8.9.4 |
| https://charts.bitnami.com/bitnami | redis | 10.6.12 |

## Chart Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| adminEmail | string | `""` |  |
| adminPassword | string | `""` |  |
| adminUser | string | `""` |  |
| affinity | object | `{}` |  |
| allowedHosts | string | `"*"` |  |
| configOverride | string | `""` |  |
| defaultFromEmail | string | `""` |  |
| emailHost | string | `""` |  |
| emailPassword | string | `""` |  |
| emailUser | string | `""` |  |
| extraConfig | object | `{}` |  |
| fullnameOverride | string | `""` |  |
| image.pullPolicy | string | `"IfNotPresent"` |  |
| image.repository | string | `"weblate/weblate"` |  |
| image.tag | string | `"4.0.2-1"` |  |
| imagePullSecrets | list | `[]` |  |
| ingress.annotations | object | `{}` |  |
| ingress.enabled | bool | `false` |  |
| ingress.hosts[0].host | string | `"chart-example.local"` |  |
| ingress.hosts[0].paths | list | `[]` |  |
| ingress.tls | list | `[]` |  |
| nameOverride | string | `""` |  |
| nodeSelector | object | `{}` |  |
| persistence.accessMode | string | `"ReadWriteOnce"` |  |
| persistence.enabled | bool | `true` |  |
| persistence.filestore_dir | string | `"/app/data"` |  |
| persistence.size | string | `"10Gi"` |  |
| podSecurityContext.fsGroup | int | `1000` |  |
| postgresql.postgresqlDatabase | string | `"weblate"` |  |
| postgresql.postgresqlPassword | string | `"weblate"` |  |
| redis.cluster.enabled | bool | `false` |  |
| redis.password | string | `"weblate"` |  |
| replicaCount | int | `1` |  |
| resources | object | `{}` |  |
| securityContext | object | `{}` |  |
| serverEmail | string | `""` |  |
| service.port | int | `80` |  |
| service.type | string | `"ClusterIP"` |  |
| serviceAccount.create | bool | `false` |  |
| serviceAccount.name | string | `nil` |  |
| tolerations | list | `[]` |  |
