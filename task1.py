import re
import textwrap

from testflows.core import *
from testflows.uexpect import ExpectTimeoutError
from testflows.asserts import error, values, raises

@TestSuite
def shell(self):
    """Suite of Shell tests.
    """
    stress_count = self.context.stress_count

    with Given("import"):
        from testflows.connect import Shell

    with Test("open"):
        with Shell() as bash:
            pass

    with Test("execute command with -a"):
        with Shell() as bash:
            bash("ls -a")

    with Test("execute command with --all"):
        with Shell(name="shell") as shell:
            shell("ls --all")

    with Test("execute command with --author"):
        with Shell() as bash:
            bash("ls --author")

def posint(v):
    v = int(v)
    assert v > 0
    return v

def argparser(parser):
    parser.add_argument("--stress-count", default=100, metavar="count", type=posint, help="number of repetitions, default: 100")

@TestModule
@ArgumentParser(argparser)
def regression(self, stress_count):
    self.context.stress_count = stress_count

    with Test("import testflows.connect"):
        import testflows.connect

    Suite(run=shell)

if main():
    Module(run=regression)