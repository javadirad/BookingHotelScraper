import logging
import json
import sys
from data import HotelInfo
from encoder import CustomEncoder
import htmlParser
import argparse
from rich import print_json

def readHtmlFile(filepath,logger):
    try:
        with open(filepath, 'r',encoding='utf-8') as f:
            html = f.read()
    except IOError as e:
        print ("I/O error({0}): {1}".format(e.errno, e.strerror))
        logger.exception("read html file error")
        return False
    except: 
        print ("Unexpected error:", sys.exc_info()[0])
        logger.exception("read html file error")
        return False
    return html

def main(inputfile,outputfile,logger):
    html= readHtmlFile(inputfile,logger)
    if not html:
        sys.exit()
    hotelInfo = HotelInfo()
    htmlParser.HtmlParser(html,hotelInfo)
    if outputfile == "":
        print_json(json.dumps(hotelInfo, indent=4, cls=CustomEncoder))
    else:
        logger.info("Start - create json file")
        try:
            with open(outputfile, "w",encoding= 'utf-8') as out_file:
                json.dump(hotelInfo, indent=4, cls=CustomEncoder,fp=out_file)
        except IOError as e:
            print ("I/O error({0}): {1}".format(e.errno, e.strerror))
            logger.exception("write json file error")
            sys.exit()
        except: 
            print ("Unexpected error:", sys.exc_info()[0])
            logger.exception("write json file error")
            sys.exit()
        logger.info("end - create json file")

def configApplication():
    logging.basicConfig(filename='Log/app.log', filemode='w',level=logging.INFO, format='%(name)s - %(levelname)s - %(message)s - %(asctime)s.%(msecs)03d',datefmt='%Y-%m-%d,%H:%M:%S')
    return logging.getLogger(__name__)

if __name__ == '__main__':
    logger = configApplication()
     
    logger.info('Application Start!')
    inputpath = "Input/Kempinski Hotel Bristol Berlin, Germany - Booking.com.html"
    inputpath = "Data.py"
    parser = argparse.ArgumentParser()
    parser.add_argument('input',nargs='?', default=inputpath,help="input Html File")
    parser.add_argument('output', nargs='?', default="",help="output Json File")
    args = parser.parse_args()
    logger.info(f'Input Html File is "{args.input}"')
    if args.output != "":
        logger.info(f'output json File is "{args.output}"')
    else:
        logger.warning('output file is not define.json will print')

    
    main(args.input,args.output,logger)
    logger.info('Application End!')
    print('Done!')



 