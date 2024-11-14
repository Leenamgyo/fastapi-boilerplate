import os

def test_verify_settings_from_env(settings):
    for key, value in settings.dict().items():
        env_value = os.environ.get(key.upper())  # os.environ은 대소문자 구분 안 함

        assert env_value == value,  \
            f"Key '{key}': Settings 값 '{value}'와 os.environ 값 '{env_value}'가 같아야 합니다."

    
    