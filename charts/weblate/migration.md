# Migration

## v0 to v1

V1 introduces breaking changes to the`values.yaml`

### Remapped values

| v0.4.16                      | v1.0.0                               |
| ---------------------------- | ------------------------------------ | ------ |
| `replicaCount`               | `weblate.replicaCount`               |
| `imagePullSecrets`           | `image.pullSecrets`                  |
| `serviceAccount.create`      | `serviceAccount.enabled`             |
| `updateStrategy`             | `weblate.updateStrategy`             |
| `podSecurityContext.*`       | `weblate.podSecurityContext.*`       |
| `containerSecurityContext.*` | `weblate.containerSecurityContext.*` |
| `adminEmail`                 | `weblate.`                           | # TODO |
| `siteTitle`                  | `weblate.siteTitle`                  |
| `siteDomain`                 | `weblate.siteDomain`                 |
| `emailHost`                  | `weblate.email.host`                 |
| `emailPort`                  | `weblate.email.port`                 |
| `emailTLS`                   | `weblate.email.tls`                  |
| `emailSSL`                   | `weblate.email.ssl`                  |
| `allowedHosts`               | `weblate.allowedHosts`               |
| `debug`                      | `weblate.debug`                      |
| `caCertSecretName`           | `weblate.caCertSecretName`           |
| `caCertSubPath`              | `weblate.caCertSubPath`              |
| `extraConfig`                | `weblate.extraConfig`                |
| `extraSecretConfig`          | `weblate.extraSecretConfig`          |
| `externalSecretName`         | `weblate.externalSecretName`         |
| `configOverride`             | `weblate.configOverride`             |
| `resources`                  | `weblate.resources`                  |
| `nodeSelector`               | `weblate.nodeSelector`               |
| `affinity`                   | `weblate.affinity`                   |
| `tolerations`                | `weblate.tolerations`                |

### Additional notes

- Redis now has its own secret containing the credentials `{{ include "weblate.fullname" . }}-redis`
- The default admin user now has its email and username saved in the weblate secret, rather than being added as ENV variables (and only the password being stored in the secret)
- The Postgres and Redis credentials were moved to separate secrets suffixed by `-postgres` and `-redis` respectively. The Bitnami charts create these secrets by default, using external PSQL/Redis will create these secrets via this chart to ensure consistency
- Configuration for using an external Redis or Postgres has changed
  - Set `[redis|postgres].enabled=false` to disable deploying the Bitnami dependencies
  - Set `weblate.external[Redis|Postgres].*` values
