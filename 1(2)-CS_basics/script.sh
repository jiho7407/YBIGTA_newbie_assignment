
# anaconda(또는 miniconda)가 존재하지 않을 경우 설치해주세요!
if ! command -v brew &> /dev/null; then
    echo "[INFO] Homebrew 설치"
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    eval "$(/opt/homebrew/bin/brew shellenv)"
fi

if ! command -v conda &> /dev/null; then
    echo "[INFO] Anaconda 설치"
    brew install --cask anaconda
    export PATH="/usr/local/anaconda3/bin:/opt/homebrew/anaconda3/bin:$PATH"
fi


# Conda 환셩 생성 및 활성화
CONDA_PATH=$(conda info --base)
source "$CONDA_PATH/etc/profile.d/conda.sh"
conda create -n myenv python=3.11 -y
conda activate myenv

## 건드리지 마세요! ##
python_env=$(python -c "import sys; print(sys.prefix)")
if [[ "$python_env" == *"/envs/myenv"* ]]; then
    echo "[INFO] 가상환경 활성화: 성공"
else
    echo "[INFO] 가상환경 활성화: 실패"
    exit 1 
fi

# 필요한 패키지 설치
pip install mypy

# Submission 폴더 파일 실행
cd submission || { echo "[INFO] submission 디렉토리로 이동 실패"; exit 1; }

for file in *.py; do
    problem_id=$(echo "$file" | cut -d'_' -f2 | cut -d'.' -f1)
    python "$file" < "../input/${problem_id}_input" > "../output/${problem_id}_output"
    echo "[INFO] ${file} 실행 완료"
done

# mypy 테스트 실행 및 mypy_log.txt 저장
mypy . > ../mypy_log.txt 2>&1
echo "[INFO] mypy 테스트 완료 및 mypy_log.txt 저장 완료"

# conda.yml 파일 생성
conda env export --name myenv --no-builds | grep -v "prefix: " > ../conda.yml
echo "[INFO] conda.yml 파일 생성 완료"

# 가상환경 비활성화
conda deactivate
echo "[INFO] 가상환경 비활성화 완료"