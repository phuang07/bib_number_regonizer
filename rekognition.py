#Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

import boto3

def detect_text(photo, bucket):
    client=boto3.client('rekognition')

    response=client.detect_text(
            #Image={'S3Object':{'Bucket':'bibnumber','Name':'bib_14285.jpeg'}},
            #Image={'S3Object':{'Bucket':'bibnumber','Name':'bib_5938.jpeg'}},
            Image={'S3Object':{'Bucket':'bibnumber','Name':'bib_38_576.jpeg'}},
            Filters={
                'WordFilter':{
                    'MinConfidence':99.6
                }
            })
                        
    textDetections=response['TextDetections']
    print ('Detected text\n----------')
    for text in textDetections:
            ## Check numeric
            print((text['DetectedText'].isnumeric()))
            if (text['DetectedText'].isnumeric()):
                print ('Detected text:' + text['DetectedText'])
                print ('Confidence: ' + "{:.2f}".format(text['Confidence']) + "%")
                print ('Id: {}'.format(text['Id']))
            print()
    return len(textDetections)

def main():

    bucket='bucket'
    photo='photo'
    text_count=detect_text(photo,bucket)
    print("Text detected: " + str(text_count))


if __name__ == "__main__":
    main()
