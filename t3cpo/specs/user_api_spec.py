from dataspec import s

# API Field definitions
mode = s("mode", {'real', 'paper'})
ChangeModeRequest = s('change_mode_request', {'mode': mode})
