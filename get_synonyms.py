import logging
from logging import handlers
import yaml
from reader.reader import Reader


with open('config.yml') as f:
    config = yaml.safe_load(f)

main_logger = logging.getLogger('synonyms.error')
main_logger.setLevel(logging.DEBUG)  # Remove this when in production
if len(main_logger.handlers) > 0:
    main_logger.handlers[0].setLevel(logging.INFO)  # terminal handler

file_logging_format = logging.Formatter(
    "[{asctime}|" + "{levelname}]" +
    " - {message}", style='{'
    )

file_logging_handler = handlers.WatchedFileHandler(
    config['storage_path'] + '/logs/synonyms_log_watchedfile'
    )

file_logging_handler.setLevel(logging.DEBUG)
file_logging_handler.setFormatter(file_logging_format)

main_logger.addHandler(file_logging_handler)


class ContextAdapter(logging.LoggerAdapter):
    def process(self, msg, kwargs):
        return ("{0} {1}".format(self.extra['context'], msg), kwargs)




if __name__ == '__main__':
    main_logger.error('test')
    rd = Reader(config)
    # rd.read_xml('hello')
    rd.read_all()


