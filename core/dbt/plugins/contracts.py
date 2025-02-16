from typing import Dict

# just exports, they need "noqa" so flake8 will not complain.
from dbt.contracts.util import ArtifactMixin as PluginArtifact, schema_version  # noqa
from dbt.contracts.util import BaseArtifactMetadata  # noqa
from dbt.common.dataclass_schema import dbtClassMixin, ExtensibleDbtClassMixin  # noqa


PluginArtifacts = Dict[str, PluginArtifact]
