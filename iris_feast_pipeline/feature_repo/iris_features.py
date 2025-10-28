from feast import Entity, FeatureView, Field, ValueType
from feast.types import Float32, Int64
from feast.infra.offline_stores.file_source import FileSource
from datetime import timedelta

# Define entity with value_type
iris_entity = Entity(
    name="iris_id",
    description="Unique ID for iris flower",
    value_type=ValueType.INT64
)

# Define data source - explicitly use CSVFormat
iris_source = FileSource(
    name="iris_source",
    path="data/iris_data_adapted_for_feast.parquet",
    timestamp_field="event_timestamp",
    created_timestamp_column="created_timestamp"
)

# Define feature view
iris_feature_view = FeatureView(
    name="iris_features",
    entities=[iris_entity],
    ttl=timedelta(days=365),
    schema=[
        Field(name="sepal_length", dtype=Float32),
        Field(name="sepal_width", dtype=Float32),
        Field(name="petal_length", dtype=Float32),
        Field(name="petal_width", dtype=Float32),
        Field(name="species", dtype=Int64),
    ],
    online=True,
    source=iris_source,
    tags={"team": "ml"}
)
