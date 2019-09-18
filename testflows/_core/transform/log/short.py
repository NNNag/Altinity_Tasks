# Copyright 2019 Vitaliy Zakaznikov (TestFlows Test Framework http://testflows.com)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from testflows._core.flags import Flags
from testflows._core.transform.log import message
from testflows._core.name import split
from testflows._core.cli.colors import color

indent = " " * 2

def color_keyword(keyword):
    return color(split(keyword)[-1], "white", attrs=["dim"])

def color_test_name(name):
    return color(split(name)[-1], "cyan", attrs=["bold"])

def color_result(result):
    if result == "OK":
        return color(result, "green", attrs=["bold"])
    elif result == "Skip":
        return color(result, "cyan", attrs=["bold"])
    # Error, Fail, Null
    return color(result, "red", attrs=["bold"])

def format_test(msg, keyword):
    _keyword = color_keyword(keyword)
    _name = color_test_name(split(msg.name)[-1])
    return f"{indent * (msg.p_id.count('/') - 1)}{_keyword} {_name} {Flags(msg.flags)}\n"

def format_result(msg, result):
    _result = color_result(result)
    _test = color_test_name(split(msg.test)[-1])
    return f"{indent * (msg.p_id.count('/') - 1)}{_result} {_test}\n"

formatters = {
    message.RawTest: (format_test, f"Test"),
    message.RawResultOK: (format_result, f"OK"),
    message.RawResultFail: (format_result, f"Fail"),
    message.RawResultError: (format_result, f"Error"),
    message.RawResultSkip: (format_result, f"Skip"),
    message.RawResultNull: (format_result, f"Null")
}

def transform():
    """Transform parsed log line into a short format.
    """
    line = None
    while True:
        if line is not None:
            formatter = formatters.get(type(line), None)
            if formatter:
                line = formatter[0](line, *formatter[1:])
            else:
                line = None
        line = yield line