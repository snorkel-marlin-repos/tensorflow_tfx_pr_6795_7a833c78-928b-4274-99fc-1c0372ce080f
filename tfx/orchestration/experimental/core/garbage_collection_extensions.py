# Copyright 2024 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The OSS alternative for garbage_collection_extensions."""

from typing import Sequence

from tfx.orchestration import metadata
from tfx.proto.orchestration import garbage_collection_policy_pb2

from ml_metadata.proto import metadata_store_pb2


def artifacts_not_in_use_in_pipeline_groups(
    mlmd_handle: metadata.Metadata,  # pylint: disable=unused-argument
    pipeline_groups: Sequence[  # pylint: disable=unused-argument
        garbage_collection_policy_pb2.GarbageCollectionPolicy.PipelineGroup
    ],
    artifacts: Sequence[metadata_store_pb2.Artifact],
) -> Sequence[metadata_store_pb2.Artifact]:
  """The OSS alternative for artifacts_not_in_use_in_pipeline_groups()."""
  return artifacts
