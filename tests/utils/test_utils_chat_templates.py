"""Module for testing chat_templates utils file."""

import unittest

from axolotl.utils.chat_templates import chat_templates
from axolotl.utils.dict import DictDefault


class ModelsUtilsTest(unittest.TestCase):
    """Testing module for chat template utils."""

    def test_default_template(self):
        cfg = DictDefault({"chat_template": "default"})
        template_str = chat_templates(cfg)
        assert template_str is None

    def test_jinja_template(self):
        cfg = DictDefault(
            {"chat_template": "jinja2", "chat_template_jinja": "{{messages}}"}
        )
        template_str = chat_templates(cfg)
        assert template_str == "{{messages}}"

    def test_user_default(self):
        cfg = DictDefault({})
        template_str = chat_templates(cfg, "chatml")
        assert template_str is not None

    def test_llama3(self):
        cfg = DictDefault({"chat_template": "llama3"})
        template_str = chat_templates(cfg)
        assert template_str is not None

    def test_cfg_choice_over_default(self):
        empty_cfg = DictDefault({})
        default_str = chat_templates(empty_cfg, "chatml")
        cfg = DictDefault({"chat_template": "llama3"})
        template_str = chat_templates(cfg, "chatml")
        assert default_str != template_str
