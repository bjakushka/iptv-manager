#
# tests for BaseModel
#

def test_base_model_repr(base_model):
    repr_result = base_model.__repr__()
    assert repr_result == '<BaseModel>', \
        'Basic implementation of __repr__ should return proper result'


def test_base_model_repr_primary_key(almost_base_model):
    repr_result = almost_base_model.__repr__()
    assert repr_result == '<AlmostBaseModel #42>', \
        '__repr__ have to print id of model if it exists'


def test_base_model_repr_no_primary_key(almost_base_model_class):
    repr_result = almost_base_model_class().__repr__()
    assert repr_result == '<AlmostBaseModel #[NONE]>', \
        '__repr__ have to display `NONE` if model has not got an id'


def test_base_model_get_model_name(base_model):
    model_name = base_model.get_model_name()
    assert model_name == 'BaseModel', \
        'Unexpected name of base model-class'


def test_base_model_get_table_name(almost_base_model):
    table_name = almost_base_model.get_table_name()
    assert table_name == 'not_existing_table', \
        'Unexpected name of table for AlmostBaseModel-class'
