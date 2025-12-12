@echo off
REM -------------------------------------------------------
REM STEP to STL Converter using FreeCAD
REM Supports argument, interactive input, and drag & drop
REM -------------------------------------------------------

REM ------------------ Load .env ------------------------
IF EXIST ".env" (
    for /f "usebackq tokens=1,* delims==" %%A in (".env") do (
        set %%A=%%B
    )
) ELSE (
    echo .env file not found. Please create it with FREECAD_PYTHON path.
    pause
    exit /b 1
)

REM Check FreeCAD Python path
IF "%FREECAD_PYTHON%"=="" (
    echo FREECAD_PYTHON not defined in .env
    pause
    exit /b 1
)

REM ------------------ Get folder path ------------------
SET "INPUT_PATH=%~1"

IF "%INPUT_PATH%"=="" (
    set /p INPUT_PATH=Enter the path to the folder containing STEP files: 
)

REM Handle drag & drop quotes
SET INPUT_PATH=%INPUT_PATH:"=%

REM Convert relative path to absolute
PUSHD "%INPUT_PATH%" 2>nul
IF ERRORLEVEL 1 (
    echo Folder not found: %INPUT_PATH%
    pause
    exit /b 1
)
SET "ABS_PATH=%CD%"
POPD

REM ------------------ Run Python script ----------------
"%FREECAD_PYTHON%" "%~dp0main.py" "%ABS_PATH%"

pause
