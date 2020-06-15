weblate
=======
Weblate is a free web-based translation management system.

Current chart version is `0.1.9`

Source code can be found [here](https://weblate.org/)

## TL;DR;

```console
$ helm repo add weblate https://helm.weblate.org
$ helm install my-release weblate/weblate
```

## Chart Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://charts.bitnami.com/bitnami | postgresql | 8.9.4 |
| https://charts.bitnami.com/bitnami | redis | 10.6.12 |

## Chart Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| adminEmail | string | `""` | Email of Admin Account |
| adminPassword | string | `""` | Password of Admin Account |
| adminUser | string | `""` | Name of Admin Account |
| affinity | object | `{}` |  |
| allowedHosts | string | `"*"` | Hosts that are allowed to connect |
| configOverride | string | `""` | Config override. See https://docs.weblate.org/en/latest/admin/install/docker.html#custom-configuration-files |
| debug | string | `"0"` | Enable debugging |
| defaultFromEmail | string | `""` | From email for outgoing emails |
| emailHost | string | `""` | Host for sending emails |
| emailPassword | string | `""` | Password for sending emails |
| emailUser | string | `""` | User name for sending emails |
| extraConfig | object | `{}` | Additional (environment) configs. See https://docs.weblate.org/en/latest/admin/install/docker.html#docker-environment |
| fullnameOverride | string | `""` |  |
| image.pullPolicy | string | `"IfNotPresent"` |  |
| image.repository | string | `"weblate/weblate"` |  |
| image.tag | string | `"4.0.4-1"` |  |
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
| redis.db | int | `1` | The Redis database number, defaults to `1`. |
| replicaCount | int | `1` |  |
| resources | object | `{}` |  |
| securityContext | object | `{}` |  |
| serverEmail | string | `""` | Sender for outgoing emails |
| service.port | int | `80` |  |
| service.type | string | `"ClusterIP"` |  |
| serviceAccount.create | bool | `true` |  |
| serviceAccount.name | string | `nil` |  |
| tolerations | list | `[]` |  |
| updateStrategy | string | `"Recreate"` |  |
