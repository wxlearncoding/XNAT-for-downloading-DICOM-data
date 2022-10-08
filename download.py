# -*- coding: utf-8 -*-

'''

The xnat package should be installed in advance!

'''

import xnat
import os



# Download Function

def DownloadData(WorkingDirectory, collectionURL, ProjectID):

    os.chdir(WorkingDirectory)

    with xnat.connect(collectionURL) as Session:

        Project = Session.projects[ProjectID]

        SubjectsList = Project.subjects.values()

        for s in SubjectsList:

            SubjectID = s.label
            print('\nEntering subject ...' + SubjectID)

            Subject = Project.subjects[SubjectID]

            ExperimentsList = Subject.experiments.values()

            for e in ExperimentsList:

                ExperimentID = e.label

                Experiment = Subject.experiments[ExperimentID]

                Experiment.download(WorkingDirectory + '\\' + ExperimentID + '.zip')


    return



if __name__ == "__main__":

    WorkingDirectory = '... '      # your working directory where you want to save the data

    collectionURL = 'https://...'  # XNAT URL

    ProjectID = '...'              # your project ID

    DownloadData(WorkingDirectory, collectionURL, ProjectID)

