from feast import Entity, FeatureView, Field, FileSource
from feast.types import Float32, Int64
from datetime import timedelta

# Define the file source
iris_data = FileSource(
    path='../data/iris_feast.parquet',
    timestamp_field='event_timestamp'
)

# Define the entity
flower = Entity(name='flower_id', join_keys=['flower_id'])

# Define the feature view
iris_view = FeatureView(
    name='iris_features',
    entities=[flower],
    ttl=timedelta(days=1),
    schema=[
        Field(name='sepal_length', dtype=Float32),
        Field(name='sepal_width', dtype=Float32),
        Field(name='petal_length', dtype=Float32),
        Field(name='petal_width', dtype=Float32),
    ],
    source=iris_data,
    online=False
)