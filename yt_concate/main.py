from pipeline.pipeline import Pipeline
from pipeline.steps.get_videolist import GetVideoList, StepException

CHANNEL_ID = 'UCBJycsmduvYEL83R_U4JriQ'

def main():
    inputs = {
        'channel_id': CHANNEL_ID
        
        }

    steps = [
        GetVideoList(),
    
        ]

    p = Pipeline(steps)
    p.run(inputs)
    
if __name__ == '__main__':
    main()