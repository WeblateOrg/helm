{{/* vim: set filetype=mustache: */}}
{{/*
Expand the name of the chart.
*/}}
{{- define "weblate.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{/*
Create a default fully qualified app name.
We truncate at 63 chars because some Kubernetes name fields are limited to this (by the DNS naming spec).
If release name contains chart name it will be used as a full name.
*/}}
{{- define "weblate.fullname" -}}
{{- if .Values.fullnameOverride -}}
{{- .Values.fullnameOverride | trunc 63 | trimSuffix "-" -}}
{{- else -}}
{{- $name := default .Chart.Name .Values.nameOverride -}}
{{- if contains $name .Release.Name -}}
{{- .Release.Name | trunc 63 | trimSuffix "-" -}}
{{- else -}}
{{- printf "%s-%s" .Release.Name $name | trunc 63 | trimSuffix "-" -}}
{{- end -}}
{{- end -}}
{{- end -}}

{{/*
Create chart name and version as used by the chart label.
*/}}
{{- define "weblate.chart" -}}
{{- printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{/*
Common labels
*/}}
{{- define "weblate.labels" -}}
app.kubernetes.io/name: {{ include "weblate.name" . }}
helm.sh/chart: {{ include "weblate.chart" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- if .Chart.AppVersion }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
{{- end }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- if .Values.labels }}
{{ toYaml .Values.labels }}
{{- end }}
{{- end -}}

{{/*
Create the name of the service account to use
*/}}
{{- define "weblate.serviceAccountName" -}}
{{- if .Values.serviceAccount.create -}}
    {{ default (include "weblate.fullname" .) .Values.serviceAccount.name }}
{{- else -}}
    {{ default "default" .Values.serviceAccount.name }}
{{- end -}}
{{- end -}}

{{- define "weblate.postgresql.fullname" -}}
{{- if .Values.postgresql.fullnameOverride }}
{{- printf "%s" .Values.postgresql.fullnameOverride | trunc 63 | trimSuffix "-" -}}
{{- else -}}
{{- printf "%s-%s" (.Release.Name | trimSuffix "-" | trunc 63 | trimSuffix "-") "postgresql" -}}
{{- end -}}
{{- end -}}

{{- define "weblate.redis.fullname" -}}
{{- if .Values.redis.fullnameOverride }}
{{- printf "%s-%s" (.Values.redis.fullnameOverride | trunc 63 | trimSuffix "-") "master" -}}
{{- else -}}
{{- printf "%s-%s-%s" (.Release.Name | trimSuffix "-" | trunc 63 | trimSuffix "-") "redis" "master" -}}
{{- end -}}
{{- end -}}
