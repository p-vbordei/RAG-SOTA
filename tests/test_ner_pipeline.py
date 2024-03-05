# RAG-SOTA/tests/test_ner_pipeline.py

import unittest
from unittest.mock import patch
from ner.ner_model import extract_and_save_entities
from ner.ner_utils import format_entities_for_storage


class TestNERPipeline(unittest.TestCase):
    @patch('ner.ner_model.predict_entities')
    @patch('ner.ner_model.save_annotations')
    def test_ner_pipeline(self, mock_save_annotations, mock_predict_entities):
        # Mock the predictions returned by the NER model
        mock_predict_entities.return_value = [
            {"span": "Amelia Earhart", "label": "person-other", "score": 0.99, "char_start_index": 0, "char_end_index": 14},
            # ... other mock entities
        ]

        # Mock the database save function to just return a fake ID
        mock_save_annotations.return_value = 'fake_annotation_id'

        # Text to process
        test_text = "Amelia Earhart flew her single engine Lockheed Vega 5B across the Atlantic to Paris."

        # Document ID (would normally be provided by your app logic)
        test_document_id = 'test_document_id'

        # Run the NER pipeline
        annotations_id = extract_and_save_entities(test_document_id, test_text)

        # Assertions to ensure the pipeline is functioning as expected
        self.assertEqual(annotations_id, 'fake_annotation_id')
        mock_predict_entities.assert_called_with(test_text)
        mock_save_annotations.assert_called_with(test_document_id, mock_predict_entities.return_value)

        # If you want to test the formatting function
        formatted_predictions = format_entities_for_storage(mock_predict_entities.return_value)
        self.assertIsInstance(formatted_predictions, list)
        self.assertGreater(len(formatted_predictions), 0)

if __name__ == '__main__':
    unittest.main()

# python -m unittest discover -s tests
### end ###