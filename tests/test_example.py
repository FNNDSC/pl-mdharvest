from pathlib import Path

from mdharvester import parser, main


def test_main(tmp_path: Path):
    # setup example data
    inputdir = tmp_path / 'incoming'
    outputdir = tmp_path / 'outgoing'
    inputdir.mkdir()
    outputdir.mkdir()
    (inputdir / 'plaintext.txt').write_text('hello ChRIS, I am a ChRIS plugin')

    # simulate run of main function
    options = parser.parse_args(['--word', 'ChRIS', '--pattern', '*.txt'])
    main(options, inputdir, outputdir)

    # assert behavior is expected
    expected_output_file = outputdir / 'plaintext.count.txt'
    assert expected_output_file.exists()
    assert expected_output_file.read_text() == '2'

def test_expected_date_format():
    #tests a standard input
    result = dateTreeBuild('20200101', '20200105', 'test_dir5')
    expected = "File successfully created"
    assert result == expected, f"Expected '{expected}', but got '{result}'"


def test_alternative_date_format():
    #tests if the user entered date in different styles
    result = dateTreeBuild('2021-01-01', '20210105', 'test_dir6')
    expected = "File successfully created"
    assert result == expected, f"Expected '{expected}', but got '{result}'"

def test_non_existent_dates():
    #tests if the user entered date that does not exist
    result = dateTreeBuild('20211312', '20211232', 'test_dir7')
    expected = "Error: Either the start or end dates do not exist"
    assert result == expected, f"Expected '{expected}', but got '{result}'"

def test_start_after_end_dates():
    #tests if the user entered date that does not exist
    result = dateTreeBuild('20211204', '20211201', 'test_dir8')
    expected = "Error: The end date is before the start date."
    assert result == expected, f"Expected '{expected}', but got '{result}'"


def test_successful_file_creation():
    result = dateTreeBuild('20220101', '20220105', 'test_dir9')
    expected = "File successfully created"
    assert result == expected, f"Expected '{expected}', but got '{result}'"



