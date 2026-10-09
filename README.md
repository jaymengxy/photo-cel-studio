# photo-cel-studio

**摄影瞬间 → 成熟手绘赛璐璐动画画面。** 将用户自己的照片转译为 1980–1990 年代日式手绘动画语法：清晰有分量的轮廓线、大面积平涂色块、硬边分层阴影和精心绘制的动画场景，同时保留人物、动物、车辆、建筑、重要物件、真实动作与镜头关系。

这个项目是一个供 Codex 等支持 Agent Skills 的环境读取的**视觉创作 Skill**，不是图片处理算法、滤镜、LUT 或独立图像生成模型。它必须配合一个**可用的图像编辑或生成工具**，才能真正输出图片。

## 安装（Codex）

克隆到你的 Codex skills 目录：

```bash
git clone https://github.com/jaymengxy/photo-cel-studio.git ~/.codex/skills/photo-cel-studio
```

或者使用 SSH（已经配置 GitHub SSH key 时）：

```bash
git clone git@github.com:jaymengxy/photo-cel-studio.git ~/.codex/skills/photo-cel-studio
```

然后重启 / 刷新 Codex 会话，使 `SKILL.md` 被扫描。也可以在支持 `~/.agents/skills/` 的 Agent Skills 运行环境中安装相同文件夹。开发中的功能请使用项目分支的文件，正式使用时以合并到 `main` 的版本为准。

**注意：** Codex 中安装 Skill ≠ 自动安装图像生成工具。需要在当前环境配置支持参考图的图像编辑能力。若当前运行环境 **no image editing capability**，本 Skill 只能提供编辑任务书，不能声称已经生成了图像。

## 使用

在支持读取本 Skill 的会话中上传一张自己的照片：

```text
使用 $photo-cel-studio 将这张照片转成复古日式赛璐璐动画剧照，
保留原始人物/动物、动作、关键物品和构图。
```

更多例子：

```text
使用 $photo-cel-studio 处理这组五张扫街照片，让线条、平涂和阴影
保持系列感；允许每张图片自动匹配合适的场景模式。
```

```text
使用 $photo-cel-studio，主模式 vehicle-mechanical，
只在原图确实存在霓虹灯和潮湿路面时采用 neon-night + rainy。
```

```text
以这张我已确认的成品为 master-lock，
只修正鱼尾，保留人物、构图、颜色和光线，其他元素保持不变。
```

## 核心设计

**全局视觉语法：** 有层次的深色轮廓、源图导出的平涂色块、清晰的硬边阴影、真实可信的人体/动物/机械结构，以及经过简化的手绘动画背景。输出默认**无文字、原图比例、保留镜头、适度风格化**。其他控制参数参见 `presets/default.yaml`。

**14 个主要场景模式（选择 1 个）：**

| 模式 | 主要用途 |
| --- | --- |
| `urban-cinematic` | 街拍 / 城市生活 |
| `quiet-dramatic` | 安静的人物与沉思场面 |
| `dynamic-action` | 动作、跑跳、运动 |
| `youth-energetic` | 儿童互动及活泼场景 |
| `sci-fi-industrial` | 工业结构与经用户同意的未来设计 |
| `everyday-still-life` | 日常器物、小型静物、容器中的鱼 |
| `landscape-cinematic` | 山海、湖泊、自然风光 |
| `pet-character` | 宠物特写和互动 |
| `vehicle-mechanical` | 车辆、交通机械 |
| `architecture-graphic` | 建筑、楼梯、桥梁、结构细节 |
| `portrait-character` | 人像及个人特色 |
| `food-lifestyle` | 食物、咖啡、餐桌 |
| `macro-nature` | 花卉、昆虫、微距自然 |
| `interior-atmosphere` | 家居与室内空间 |

**6 个可选氛围模式（自动 0–2 个）：** `neon-night`、`golden-hour`、`rainy`、`snowy`、`misty`、`backlit`。

**自动选择尊重证据：** 真实照片里没有雨、霓虹或落日时，不会自动捏造这些条件。用户可以明确要求改变天气或时代，但那是有意的再创作，不是忠实纪录转换。

## Adding a mode / 扩展新模式

1. 复制 `templates/mode-template.md` 到 `modes/<new-mode>.md`，用新题材的具体边线、色彩、阴影、保真/禁止规则替换占位符。
2. 在 `references/scene-modes.md` 增加一条注册记录和邻近模式的分流依据。
3. 在 `tests/scenarios.md` 新增正向与反向场景，运行结构测试。
4. **不要修改** 根目录 `SKILL.md` 来注册新模式，它只按需读取注册表中匹配的文件。

新增氛围时对 `templates/atmosphere-template.md`、`atmospheres/<id>.md`、`references/atmosphere-selection.md` 做类似操作。所有氛围自动触发必须有可见证据。

## 开发与测试

只依赖 Python 3 标准库即可运行结构验证：

```bash
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

详细的五张街拍照片场景、其他模式组合、手动图像评估表见 `tests/scenarios.md`。测试照片应保留在本地或当前会话，不要上传到公开代码仓库。

## Limitations / 已知限制

- Skill 自身只提供决策和 prompt 结构，**no image output** without a connected image-edit model.
- Prompt 无法保证像素级人物身份精度、局部像素锁定、读清模糊文字、被遮挡人数或生物计数。
- 成果必须视觉审核；通过文件结构测试不代表图片艺术质量测试已通过。
- 不提供未经同意的新人物、天气、品牌、假地点或虚构文案。
- 参考 80–90 年代成熟赛璐璐动画的通用视觉特性，不复刻具体动画作品角色、画面或其官方元素。
- 原始摄影图片和成品不自动发布到本仓库。

## 设计和计划

- [设计规范](docs/superpowers/specs/2026-10-10-photo-cel-studio-design.md)
- [v0.1 开发计划](docs/superpowers/plans/2026-10-10-photo-cel-studio-v0.1.md)
