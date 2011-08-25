from pandac.PandaModules import loadPrcFileData

loadPrcFileData("", "sync-video #f")
loadPrcFileData("", "show-frame-rate-meter #t")
loadPrcFileData('', 'bullet-enable-contact-events true')

from gamecode.Game import Game

if __name__=='__main__':
    winst = Game()
    run()
