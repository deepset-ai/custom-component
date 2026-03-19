# SPDX-FileCopyrightText: 2026-present AUTHOR <your@email.com>
#
# SPDX-License-Identifier: Apache-2.0

# TODO: Add tests for your component(s). Below is a skeleton to get you started.
#
# import pytest
#
# from haystack_integrations.components.example import MyComponent
#
#
# class TestMyComponent:
#     def test_init(self):
#         component = MyComponent()
#         assert component is not None
#
#     def test_run(self):
#         component = MyComponent()
#         result = component.run(...)
#         assert "output_name" in result
#
#     def test_to_dict(self):
#         component = MyComponent()
#         data = component.to_dict()
#         assert data is not None
#
#     def test_from_dict(self):
#         component = MyComponent()
#         data = component.to_dict()
#         deserialized = MyComponent.from_dict(data)
#         assert deserialized is not None
#
#     @pytest.mark.integration
#     def test_run_with_real_service(self):
#         """Integration tests that require external services or API keys."""
#         ...
